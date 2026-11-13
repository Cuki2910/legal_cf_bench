# V2 — protocol triển khai đã duyệt, không thay v1

## Phạm vi

Rule application bằng tiếng Anh trên luật tổng hợp cho trước; không luật thật, không RAG, không Challenger LLM. Không đo true reasoning hay cơ chế nội tại. Các sửa dựa trên `GOLD_ADJUDICATION_v1.md`; user đã duyệt phương án, không phải mọi item mới tự động được chứng nhận.

## Dataset và tách dữ liệu

- Toàn bộ schema từng xuất hiện ở v1 chuyển thành **dev**, kể cả 8 schema từng gọi là test. Đã xem phản hồi model nên không dùng lại như unseen test.
- Schema mới chỉ là held-out đối với **API evaluation v1**, không phải tác giả benchmark chưa biết gold. Tác giả phải thấy gold để viết/kiểm dữ liệu.
- T/F/U theo Kleene trên read-once formulas. Kiểm độc lập bằng liệt kê Boolean completions cho mọi assignment T/F/U. Chỉ nhận formulas read-once để tránh đánh đồng supervaluation và Kleene trên expressions có atom lặp.
- Fact IDs ổn định theo slot; khi thêm/bỏ một proposition không đánh số lại các fact còn lại.
- Một edge chỉ được khác đúng một fact ID; không drop dependent facts. Nếu không thể giữ coherence thì phải sửa template, không lén coi context-repair là minimal pair.
- Một stimulus theo content hash, gọi model tối đa một lần trong mỗi prompt/repetition. Nhiều edge có thể trỏ cùng stimulus nhưng không tăng số lần gọi.

## Metric cố định trước model run

- **Unique-stimulus accuracy** và base accuracy: mỗi stimulus có một trọng số.
- M1/flip, M2/near, M3/I1 và I2: báo riêng target accuracy, pair-correct (base và intervention đều đúng), conditional trên base đúng. Target accuracy không đồng nghĩa trực tiếp model đã flip/stay so với answer base của nó.
- M1 headline: pair-correct trên F/S; M2 headline: pair-correct trên N; M3 headline: pair-correct trên I1. I2, target/conditional là số phụ. Việc đổi operationalization này là v2 mới, không thay nhãn/điểm v1.
- Pair metrics có edge weighting; unique accuracy có stimulus weighting. Không trộn hai mẫu số.
- Cluster bootstrap theo schema, seed cố định, 2.000 samples; in số cluster. Ít schema thì CI không đủ để claim khái quát/xếp hạng.
- Không dùng M5 để kết luận năng lực/explanation alignment. Lưu explanation raw để qualitative audit.
- pA/pB là prompt variation, không thay thế repetition. Nếu qua gate chạy API: cùng 3 route đã dùng, pA/pB và repetition 1/2; không chọn một prompt hoặc một lần chạy đẹp. Prompt stability và repeat agreement phải báo riêng.
- Oracle và const-yes/no/undetermined kiểm pipeline; oracle không chứng minh gold tiếng Anh đúng. Lexical baseline v1 không chuyển nguyên vì dùng metadata gold base; nếu muốn thêm baseline mới phải khai báo trước API evaluation.

## Evidence và resumability

Mỗi record mới lưu: dataset digest, stimulus ID, prompt version, repetition, request body (không auth header), response envelope hoặc SSE events, raw text, parsed answer và thời điểm hoàn tất. Provider identity từ envelope chỉ là self-reported metadata, không bằng chứng xác minh độc lập.

Không retry nội dung sai/JSON lỗi để chọn câu trả lời khác. Nếu request fail thì dừng và giữ các record đã ghi; resume chỉ các ID chưa có. Request có thể đã được provider thực hiện dù client chưa ghi nhận; không hứa exactly-once qua network.

Output build không ghi đè nội dung khác. Manifest hash dataset và code; không chỉnh manifest để “lách” human audit. Gate mặc định `allow_api=false`, `human_item_review=pending`, `second_reviewer=unverified`.

## Trạng thái hoàn thành

Code/dataset/offline checks là phần trợ lý có thể hoàn thành. Người kiểm thứ hai và xác nhận từng item mới là phần **chưa kiểm chứng** nếu chưa có bằng chứng; không dùng một lần “goal/xong hết” làm chứng nhận chúng đã xảy ra. API run bị chặn đến khi human item review hoàn tất và được duyệt rõ ràng. Không tự commit/push.

## Lệnh chạy

Từ `legal_cf_bench/`:

```sh
python3 -W error::ResourceWarning -m unittest discover -s tests
python3 -m lcb.v2 build
python3 -m lcb.v2 check
# Sau review và phê duyệt manifest, không chạy trước:
python3 -m lcb.v2 run --model 'cx/gpt-6.1-sol' --split test --prompt pA --repeat 1
python3 -m lcb.v2 report --raw data/v2/runs/<run-id>.jsonl --split test
```

Không coi ví dụ lệnh API ở đây là run đã thực hiện. Thông tin về nguồn ngoài/phù hợp luật thật: **chưa kiểm chứng**; các con số sau build nằm trong `data/v2/manifest.json`, `data/v2/dataset.json`, `data/v2/baselines.json`.
