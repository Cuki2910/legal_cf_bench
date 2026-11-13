# Thiết kế benchmark v1 (bản nháp, CHƯA chạy, CHƯA chốt)

Trạng thái: đề xuất thiết kế sau khi pilot v0 lộ lỗi. Mọi quyết định ở mục 15 cần Kiệt (và thầy) xác nhận.
Ngôn ngữ an toàn: chỉ nói về *observable decision behavior*, *counterfactual sensitivity*, *behavioral consistency*, *legally meaningful factual intervention under a stated rule*. Không claim đo "true reasoning" hay model "dùng" factor nào bên trong.

---

## 1. Mục tiêu và phạm vi

Đo hành vi trả lời của một mô hình khi **luật cho trước trong prompt** và **một tình tiết bị can thiệp có kiểm soát**:

1. Tình tiết làm đổi kết quả theo luật đó thì câu trả lời có đổi không (relevant-fact sensitivity).
2. Tình tiết trông giống liên quan nhưng không đổi kết quả thì câu trả lời có giữ nguyên không (near-miss specificity).
3. Tình tiết không liên quan thì câu trả lời có giữ nguyên không (irrelevant-fact robustness).
4. Tình tiết mà mô hình *nói* là quyết định có khớp với tình tiết quyết định thật theo luật không (reported deciding-fact agreement). Đây là điều model khai báo, không phải bằng chứng về cơ chế bên trong.

Không phải mục tiêu v1: luật thật, retrieval/RAG, tiếng Việt, sinh can thiệp bằng LLM (Challenger), kết luận về "faithfulness".

## 2. Chẩn đoán pilot v0 (vì sao kết quả không dùng được)

| # | Lỗi | Bằng chứng trong v0 |
|---|---|---|
| D1 | Gold sai/mơ hồ, gán tay | 3/10 case: `hotel_safe` (rule "only if" = điều kiện cần, gold `yes` đòi điều kiện đủ), `necessity` (facts không nói cố ý/sơ suất nhưng gold `yes`), `dismissal` (trộm tiền được thêm nhưng không nói là lý do sa thải). Sol trả lời chặt hơn gold ở cả 3. |
| D2 | Không có đáp án "chưa đủ dữ kiện" | Ép yes/no nên model đúng về mặt logic vẫn bị chấm sai (D1). |
| D3 | Irrelevant quá dễ | "car red", "shirt blue". Chỉ đo được ngưỡng sàn, gần như chắc chắn đạt 100%. |
| D4 | Không có near-miss | Relevant challenge luôn dùng đúng từ khóa của rule ("written", "permit"). Model chỉ cần khớp từ khóa là qua. Không tách được "nhạy với ý nghĩa pháp lý" khỏi "khớp từ vựng". |
| D5 | Mất cân bằng nhãn | Base gold: 7/10 `yes`. Baseline `const-yes` đã cao. |
| D6 | n = 10 | CI Wilson 95% rộng (vd 10/10 → [0.72, 1.0]). Không xếp hạng được hai model. |
| D7 | Không có độ khó | Luna 10/10 mọi chỉ số: trần (ceiling). Benchmark không phân biệt được gì. |
| D8 | Proxy giải thích bằng từ khóa | `keyword_proxy` không phải alignment. |
| D9 | Metric có điều kiện trên base đúng | Mẫu co lại, không báo cáo bản không điều kiện. |
| D10 | Không kiểm soát vị trí/diễn đạt | Tình tiết can thiệp luôn ở cuối; chỉ một prompt. |

Hệ quả: số liệu v0 (Sol 9/10, 7/9, 9/9; Luna 10/10 ×4) **không dùng làm kết quả hiệu năng**. Chỉ dùng như phát hiện thiết kế.

## 3. Nguyên tắc thiết kế

- **P1. Gold do chương trình tính, không gán tay.** Mỗi rule được hình thức hóa thành công thức logic trên các nguyên tử (atom). Gold = đánh giá công thức trên phép gán giá trị của atom.
- **P2. "Relevant" được định nghĩa thao tác, không phải tuyên bố pháp lý.** Một can thiệp là *relevant* khi và chỉ khi nó đổi giá trị công thức dưới rule đã nêu. Đây là *legally meaningful factual intervention under a stated rule*, không phải "đúng theo luật thật".
- **P3. Minimal pair.** Mỗi can thiệp làm đổi kết quả có một cặp near-miss gần như giống hệt về bề mặt nhưng không đổi kết quả.
- **P4. Ba giá trị đáp án** `yes` / `no` / `undetermined`, với quy tắc rõ trong prompt: tình tiết không nêu = *unknown*, không phải *false*.
- **P5. Tiêu chí kết quả đặt trước (pre-specified).** Metric chính, baseline và ngưỡng "benchmark có phân biệt được" khai báo trước khi chạy model.
- **P6. Không dùng model để tạo hay xác nhận gold** (tránh vòng tròn). Model chỉ là đối tượng được đo.

## 4. Đặc tả rule và dữ liệu

### 4.1 Quy ước viết rule (tránh lỗi `hotel_safe`)
Chỉ dùng 3 khuôn kết nối, mỗi khuôn có nghĩa logic cố định và được ghi trong prompt:

- `X if A and B.` = A ∧ B ⇒ X (đủ, chưa nói về cần).
- `X, unless E.` = X ∧ ¬E (E là ngoại lệ loại trừ).
- `X if and only if A.` = A ⇔ X.

Cấm: "only if" đứng một mình, "may" mơ hồ, mệnh đề phủ định kép. Mỗi rule được kiểm tra bằng bảng chân trị trước khi vào dataset.

### 4.2 Schema (YAML/JSON)
```
schema_id, tier, rule_text, question_text
atoms: {A1: {desc, true_text[], false_text[]}, A2: ...}   # nhiều cách diễn đạt mỗi giá trị
formula: "A1 and not A2"                                  # 3-valued Kleene: T/F/U
deciding_atom_rule: cách xác định atom quyết định cho gold alignment
base: {A1: T, A2: F, ...}                                 # phép gán cơ sở, có thể có U
```
Gold = `eval(formula, assignment)` → {yes, no, undetermined}. Khung mô tả case được sinh bằng template từ assignment, không viết tay từng câu.

### 4.3 Ví dụ một schema (tenancy)
- Rule: "A landlord may evict a tenant who pays rent more than 30 days late, unless the landlord accepted the late payment in a signed written notice."
- Atoms: A1 = thanh toán trễ > 30 ngày; A2 = chủ nhà chấp nhận bằng văn bản ký tên. Formula: `A1 and not A2`.
- Base (A1=T, A2=F) → `yes`. Các item:

| Loại | Can thiệp | Gold | Ghi chú |
|---|---|---|---|
| flip | "The landlord signed a written notice accepting the late payment." | `no` | A2: F→T |
| flip (atom khác) | "T actually paid 12 days late." | `no` | A1: T→F |
| near-miss (khác dạng) | "The landlord orally told T the late payment was fine." | `yes` | A2 vẫn F vì không văn bản |
| near-miss (biên số) | "T paid 31 days late." (base 45) | `yes` | vẫn > 30 |
| irrelevant plausible | "T had paid on time every month for five years." | `yes` | trông liên quan, rule không nhắc |
| irrelevant lexical | "T's apartment is on the fifth floor." | `yes` | thuộc tính vô hại |
| underdetermined base | base chỉ nói "T paid rent late" (A1=U) → `undetermined`; can thiệp "45 days late" → `yes` | | kiểm tra không đoán bừa |

## 5. Taxonomy can thiệp

| Mã | Loại | Định nghĩa | Gold so với base |
|---|---|---|---|
| F | flip | đổi giá trị 1 atom làm đổi công thức | đổi |
| N1 | near-miss khác dạng | chạm đúng chủ đề của atom nhưng không thỏa điều kiện (oral vs written) | giữ |
| N2 | near-miss biên số | đổi số nhưng không qua ngưỡng | giữ |
| N3 | boundary-flip | đổi số vượt ngưỡng (29 vs 31 ngày) | đổi |
| I1 | irrelevant plausible | trông có ý nghĩa pháp lý nhưng atom không có trong công thức | giữ |
| I2 | irrelevant lexical | thuộc tính vô hại | giữ |
| S | supply | cung cấp atom đang U làm công thức xác định | `undetermined` → yes/no |
| (v1.1) C | compound | F + I, hoặc hai F triệt tiêu nhau (feature interaction) | tính từ công thức |

Mỗi can thiệp có `position` ∈ {end, middle}: kiểm soát thiên vị vị trí.
Ghi chú liên hệ literature: N1/I1 phản ánh mối lo OOD và "hindsight/feature interaction" khi can thiệp counterfactual (Paper 4). Mỗi can thiệp được sinh bằng template, không phải bằng LLM, nên chưa phải Challenger.

## 6. Bậc độ khó (chống trần, D7)

| Tier | Mô tả | Số schema |
|---|---|---|
| T1 | 1 atom (kiểu `parking`) | 3 |
| T2 | 1 điều kiện + 1 ngoại lệ (kiểu `tenancy`) | 4 |
| T3 | ≥ 3 atom, ngoại lệ của ngoại lệ (kiểu `insurance_late`) | 3 |
| T4 | khung tình tiết dài ~150 từ, atom quyết định chôn giữa, nhiều chi tiết gây nhiễu | 2 |

Thêm cờ **rule-override**: ở ~1/3 schema, rule ngược với trực giác pháp lý thường gặp (vd thời hiệu 10 năm, không phải 3). Kiểm tra model làm theo rule cho trước hay theo tiên nghiệm.

## 7. Prompt và định dạng trả lời

- Tình tiết đánh số `F1..Fn`; can thiệp là `F(n+1)` (end) hoặc chèn vào giữa và đánh số lại (middle).
- Hướng dẫn cố định: "Apply ONLY the rule. A fact not stated is unknown, not false. If the stated facts do not settle the question under the rule, answer `undetermined`."
- Trả lời JSON: `{"answer": "yes|no|undetermined", "deciding_fact": "F<k>" hoặc "none", "explanation": "..."}`.
- `deciding_fact` chọn từ danh sách ID → khớp chính xác với gold, thay cho keyword proxy.
- Hai phiên bản prompt diễn đạt khác (`pA`, `pB`) để đo độ nhạy với diễn đạt. Tăng `PROMPT_VERSION`.
- Nhiệt độ 0, `max_tokens` đủ cho JSON. Lưu raw đầy đủ.

## 8. Metric (khai báo trước)

Mọi tỉ lệ báo cáo **cả không điều kiện lẫn có điều kiện** trên base đúng.

| Mã | Tên | Định nghĩa |
|---|---|---|
| M0 | Base accuracy | đáp án đúng gold ở tình tiết cơ sở |
| M1 | Flip sensitivity | đúng gold mới trên F, N3, S |
| M2 | Near-miss specificity | giữ đúng gold trên N1, N2 |
| M3 | Irrelevant robustness | giữ đúng gold trên I1, I2 (báo riêng I1 và I2) |
| M4 | Case-level consistency | tỉ lệ case mà base và mọi can thiệp đều đúng |
| M5 | Deciding-fact agreement | `deciding_fact` khớp atom quyết định gold (trên item mà answer đúng) |
| M6 | Prompt stability | tỉ lệ item giữ đáp án giữa `pA` và `pB` |
| M7 | Direction asymmetry | M1 tách theo hướng yes→no vs no→yes |

Headline (tối đa 3, để tránh chọn số đẹp sau khi thấy dữ liệu): **M1, M2, M3(I1)**. Còn lại là phụ.

## 9. Baseline và kiểm tra benchmark có "phân biệt được"

Baseline không dùng model:
- `const-yes`, `const-no`, `const-undetermined`.
- `oracle` (phải đạt 100%, kiểm thử pipeline).
- `keyword-trigger`: đổi đáp án nếu can thiệp chứa từ khóa của rule. Nếu baseline này vẫn cao trên N1 thì near-miss thiết kế chưa đủ khó.

Tiêu chí để benchmark được coi là có thông tin (đặt trước, chạy trên ≥ 3 model khác cỡ, khác dòng):
- Không baseline nào đạt M1, M2, M3 cùng lúc ≥ 0.70.
- Không model nào đạt ≥ 0.98 ở cả M0–M3 (không trần).
- Có ít nhất một tier/loại can thiệp mà khoảng cách giữa 2 model vượt CI.
Không đạt → thiết kế khó hơn (tier, near-miss) trước khi báo cáo bất cứ gì.

## 10. Thống kê

- Item trong cùng schema tương quan, nên **cluster bootstrap theo schema** (hoặc Wilson trên cấp case làm đối chiếu), không coi mọi item độc lập.
- So hai model: paired (cùng item) bằng McNemar hoặc paired cluster bootstrap. Báo cáo kích thước hiệu ứng và CI, không chỉ p-value.
- Chạy lặp 2 lần cùng cấu hình để ước lượng không tất định của gateway.
- Báo cáo mọi loại can thiệp, kể cả loại kết quả xấu.

## 11. Kiểm soát chất lượng gold

1. Unit test: công thức ↔ bảng chân trị; mỗi can thiệp loại F phải đổi gold, loại N/I phải giữ gold (code `validate()` mở rộng).
2. Kiệt đọc 100% item sinh ra, đánh dấu câu mơ hồ. Mục tiêu: 0 item bị gắn cờ còn lại.
3. Kiểm tra mẫu 20% item bởi người thứ hai (thầy hoặc bạn học luật nếu có). Chưa có thì ghi rõ "chưa kiểm chứng bởi chuyên gia pháp lý".
4. Không dùng agreement giữa các LLM để chứng minh gold đúng. Chỉ dùng để *phát hiện* item đáng nghi.

## 12. Kích thước đề xuất

- 12 schema × 3 base (yes / no / undetermined) = 36 case.
- Mỗi case ≈ 6 can thiệp → ≈ 250 item/prompt; × 2 prompt = ≈ 500 lượt gọi/model; ~ 20–30 phút/model, chi phí thấp.
- Số item F+N3+S ≈ 90–100, N ≈ 70, I ≈ 70. CI nửa-rộng ≈ ±0.07–0.10 ở tỉ lệ ~0.9 (ước lượng thô, sẽ tính lại bằng bootstrap).

## 13. Mối đe dọa tính hợp lệ (phải nêu trong báo cáo)

- Luật tổng hợp, tiếng Anh, rule đưa sẵn trong prompt: kết quả không tổng quát sang luật thật, tiếng Việt hay RAG.
- "Relevant" là định nghĩa thao tác theo công thức, không đo "relevance pháp lý thật".
- Template đơn điệu: model có thể học mẫu câu. Giảm bằng nhiều cách diễn đạt mỗi atom, nhưng không loại hết.
- Gold chưa qua chuyên gia pháp lý (nếu chưa làm mục 11.3).
- 1–3 model, một gateway, nhiệt độ 0: không suy ra về "model nói chung".
- `deciding_fact` là lời khai của model, không phải bằng chứng về yếu tố nội tại.
- Không có phần Challenger. v1 là tập can thiệp cố định.

## 14. Kế hoạch triển khai

| Bước | Việc | Ước lượng |
|---|---|---|
| 1 | Chốt rule-writing convention, 12 schema trên giấy (atom, công thức, bảng chân trị) | 0.5–1 ngày |
| 2 | Code: evaluator 3-valued, sinh case/can thiệp từ template, `validate()` mới | 1 ngày |
| 3 | Baseline không-model + oracle + test | 0.5 ngày |
| 4 | Kiệt audit 100% item, sửa | 0.5 ngày |
| 5 | Pilot trên 3 model, kiểm tra tiêu chí mục 9 | 0.5 ngày |
| 6 | Quyết định: chạy chính thức hoặc làm khó hơn | |

## 15. Cần Kiệt quyết định

1. Chấp nhận đáp án 3 giá trị (`undetermined`)? Khuyến nghị: có.
2. Chấp nhận định nghĩa "relevant = đổi kết quả theo công thức của rule cho trước"? Khuyến nghị: có, ghi rõ giới hạn.
3. Quy mô 36 case/≈250 item (mục 12) có đủ cho bài midterm/seminar? Khuyến nghị: có.
4. Sinh can thiệp bằng template, không LLM, ở v1? Khuyến nghị: có (tránh vòng tròn, giữ Challenger làm phần sau).
5. Có người kiểm gold thứ hai (thầy/bạn học luật) không? Nếu không, báo cáo ghi "chưa kiểm chứng".
6. Báo cáo midterm: ghi pilot v0 như một phát hiện thiết kế (D1–D10), không ghi số liệu hiệu năng? Khuyến nghị: có.
