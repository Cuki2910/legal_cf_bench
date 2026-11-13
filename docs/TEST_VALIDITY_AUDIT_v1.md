# Audit tính hợp lệ test v1 — sau chạy, không đổi gold

## Kết luận

**Chưa dùng v1 để xếp hạng năng lực model.** Một số facts không xác định giá trị atom mà template gán cho chúng. Do đó điểm hiện tại trộn khả năng áp dụng luật với cách xử lý tiền giả định/thiếu dữ kiện. Đây là kiểm tra kỹ thuật bằng trợ lý, không phải xác minh bởi chuyên gia pháp lý; độ đúng pháp lý vẫn **chưa kiểm chứng**.

Không thay test, gold, parser hoặc raw trong audit này. Hash đã kiểm tra khớp `TEST_FREEZE.txt`. Các điểm và CI cũ vẫn được giữ để tránh chọn kết quả sau khi xem dữ liệu. Không suy ra toàn bộ chênh lệch điểm do các lỗi dưới đây; chưa có bộ gold đã adjudicate để định lượng phần đó.

## 1. Các cờ ngữ nghĩa đã đối chiếu trực tiếp

| Item mẫu | Gold hiện tại | Vấn đề facts → atom | Bằng chứng raw pA |
|---|---|---|---|
| `hotel_safe/yes/base` | yes | Rule yêu cầu đồng hồ trong safe **lúc bị trộm**, nhưng fact chỉ nói gửi safe **ngày đầu**. Thiếu liên kết thời gian. | Sol: “depositing the watch on the first day does not establish that it was in the hotel safe at the time of the theft.” Haiku suy từ việc đã gửi safe sang đủ điều kiện. |
| `debt_limitation/yes/base` | yes | “never wrote to the creditor” không loại hết việc xác nhận nợ bằng văn bản cho người khác; rule không giới hạn người nhận. | Sol: “does not establish whether the debtor acknowledged the debt in writing other than by writing to the creditor”. Haiku: “F3 confirms no written acknowledgment occurred”, rộng hơn fact. |
| `dismissal_no_notice/yes/base` | yes | “no written agreement … beyond the standard employment contract” không loại điều khoản bảo vệ trong chính hợp đồng chuẩn. | Sol: “does not establish whether the standard employment contract included written job protection signed by M.” Haiku suy “no written job-protection agreement exists”. |
| `contract_breach/yes/base` và `contract_breach/no/base` | yes / no | Sự kiện hằng năm hoặc chưa từng xảy ra trong vùng không tự xác định foreseeability của sự kiện cụ thể. | Sol ở yes/base: “the stated facts do not establish whether the event was unforeseeable”. Haiku pA cũng trả undetermined, nhưng giải thích có mâu thuẫn. |

Vị trí nguồn: `lcb/rules.py:188-208` (hotel), `:109-120` (debt), `:165-183` (dismissal), `:144-160` (contract). Phản hồi đầy đủ trong `results/v1__*__test_pA/raw.jsonl`, tìm theo item ID; bảng chỉ trích phần cần thiết.

**Không gán lại gold tự động:** đây là các cờ đủ để yêu cầu adjudication, không phải một bộ nhãn mới. Không phải mọi câu trả lời `undetermined` đều đúng; cũng không phải mọi điểm khớp gold đều chứng minh suy luận đúng.

## 2. Trùng stimulus và trọng số

Kiểm tra toàn bộ prompt pA sinh từ test hiện tại:

- 239 ID nhưng chỉ **183 prompt khác nhau**.
- **46 nhóm trùng**, chứa tổng cộng **102 item**. 102 là số item nằm trong nhóm trùng, không phải số bản sao dư; số bản sao dư là 56.
- Ví dụ cùng stimulus: `hotel_safe/yes/base`, `hotel_safe/no/F.A1`, `hotel_safe/undetermined/S.A2T`.

Các nhãn base/F/S khác nhau có thể hợp lý trong phân tích cặp can thiệp. Tuy nhiên chúng **không phải quan sát nội dung độc lập**; pooled accuracy tạo trọng số ngầm cho stimulus được lặp. Cluster bootstrap theo schema giữ phụ thuộc trong cluster nhưng không loại trọng số này hay sửa gold mơ hồ. Không dedupe hồi tố headline đã đóng băng; phiên bản kế tiếp cần định trước metric theo edge/cặp và metric theo stimulus duy nhất.

## 3. Minimal pair chưa được bảo đảm

`lcb/v1.py:111-118` có thể đổi một atom rồi **bỏ các câu phụ thuộc** qua `needs`. Ví dụ `contract_breach/yes/F.A1` không chỉ thay A1 mà còn bỏ các fact E1/E2. Đây không phải one-sentence factual edit. Near-text còn có thể thêm chi tiết khác ngoài atom, nên “minimal” hiện chỉ là ý định thiết kế, chưa phải ràng buộc đã validate.

`validate()` (`lcb/v1.py:127-138`) chỉ kiểm tra ID/nhãn và gold đổi hay giữ. Nó không chứng minh tương đương ngữ nghĩa, tính đầy đủ facts, hay minimality của can thiệp.

## 4. M5 là proxy hỗn hợp, không phải alignment đã xác lập

- Parser (`lcb/v1.py:156-157`) chỉ nhận **một** ID dạng F<number>. Haiku trả `F4, F5, F7` ở `hotel_safe/yes/base`, hoặc `F2, F3, F4` ở `dismissal_no_notice/yes/base`: đó là vi phạm output schema, không tự chứng minh chọn sai tình tiết. Các base này không nằm trong mẫu M5; chúng chỉ minh họa cách trả nhiều fact trong raw.
- M5 (`lcb/v1.py:249-252`) chỉ chấm flip có answer đúng, gold mới xác định, và đòi chọn đúng **fact bị sửa**. Nó không biểu diễn mọi tập fact đủ để quyết định. Chọn nhiều fact có thể có nội dung hợp lý nhưng vẫn sai format.
- Mẫu số phụ thuộc vào độ đúng đáp án của từng model; gold mơ hồ ảnh hưởng việc model nào được đưa vào mẫu. Không dùng Sol M5 cao để suy ra explanation faithful hơn.

## 5. Hành động tiếp theo — chưa thực hiện

1. Giữ v1 nguyên trạng như một kết quả **validation/design audit**, không dùng thứ hạng để claim năng lực pháp lý.
2. Kiệt/người kiểm thứ hai adjudicate các cờ facts↔atoms và kiểm toàn bộ item trước API run kế tiếp.
3. V2 viết rõ mốc thời gian, phạm vi phủ định và điều kiện đã biết; không tăng “độ khó” bằng việc thiếu tiền đề.
4. Định trước can thiệp một fact, việc xử lý dependency, trọng số stimulus trùng, M5 theo tập fact và chấm format tách biệt.
5. Tập v1 đã được xem kết quả nên không còn là unseen test cho v2; nếu thay thiết kế, cần held-out schemas mới. Không chỉnh đến khi ra thứ hạng mong muốn.

## Nguồn cục bộ và phạm vi kiểm tra

- Source of truth: [`rules.py`](../lcb/rules.py), [`v1.py`](../lcb/v1.py).
- Kết quả giữ nguyên: [`TEST_RESULTS_v1.md`](TEST_RESULTS_v1.md), [`TEST_FREEZE.txt`](TEST_FREEZE.txt).
- Đã đối chiếu trực tiếp 4 item mẫu pA ở Sol và Haiku; đếm trùng trên toàn bộ 239 prompt test; lượt kiểm trước xác nhận đủ 6 run × 239 ID và hash freeze khớp. Audit của trợ lý không thay thế kiểm chứng gold bởi người thứ hai.
