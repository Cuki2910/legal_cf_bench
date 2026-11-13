# Phiếu adjudication gold v1 — Kiệt đã xác nhận phương án sửa và protocol, chưa triển khai v2

## 0. Mục đích và trạng thái

**Giữ nguyên dữ liệu v1. Chưa chạy model cho phiên bản mới.** Kiệt đã trả lời “xác nhận” sau khi nhận phiếu này: ghi nhận phê duyệt phương án sửa A01–A05, các hướng xử lý trong bảng coverage và protocol B01–B05. Không diễn giải phê duyệt này thành xác nhận toàn bộ gold của các item sẽ sinh trong v2.

Trạng thái: **PHƯƠNG ÁN ĐÃ ĐƯỢC KIỆT XÁC NHẬN; CHƯA TRIỂN KHAI/VALIDATE V2**. Kiểm tra toàn bộ item mới và người thứ hai: **chưa kiểm chứng**. Đây không phải kết quả chuyên gia pháp lý.

Lần chạy trước đã tiến hành khi chưa xác nhận bước human audit; đó là thiếu sót trong quy trình thực hiện. Unit test/oracle không thay thế bước này. Không dùng chi phí API đã bỏ ra làm lý do giữ claim hiệu năng.

### Cách ghi quyết định

Mỗi mục chọn: `giữ` / `sửa` / `loại` / `cần thảo luận`; ghi lý do, người kiểm và phiên bản câu chốt. Không chỉ ghi “model đồng ý”.

Một câu được nhận làm T/F khi facts **xác định** giá trị đó theo định nghĩa atom. Không nêu ≠ F. Phải kiểm cả đoạn case, vì câu khác có thể tiết lộ atom đang bị bỏ để tạo U hoặc tạo mâu thuẫn.

Nguồn cục bộ: [rules.py](../lcb/rules.py), [v1.py](../lcb/v1.py), [ITEMS_v1.md](ITEMS_v1.md), [audit](TEST_VALIDITY_AUDIT_v1.md). Các câu sửa là **proposed methodology**, không phải phát biểu về luật thật; tính phù hợp pháp lý ngoài rule tổng hợp: **chưa kiểm chứng**.

## 1. Các quyết định ngữ nghĩa ưu tiên

### A01 — hotel_safe: liên kết thời gian của vị trí đồng hồ

- Nguồn: `rules.py:188-208`.
- Atom: A1 = **chiếc đồng hồ bị trộm ở trong hotel safe lúc bị trộm**.
- Hiện tại T: “G had deposited the watch ... on the first day of the stay.” Không xác định vị trí lúc theft.
- Đề xuất T chuẩn: `The watch that was stolen was in the hotel safe at reception at the time of the theft.`
- Đề xuất T near: `The stolen watch was inside a sealed envelope with G's passport in the hotel safe at reception at the time of the theft.`
- Đề xuất F chuẩn: `At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.`
- Đề xuất F near: `At the time it was stolen, the watch was in the locked wardrobe drawer in room 412, not in the hotel safe.`
- Đề xuất context: `G's watch was stolen during the stay.` Xác định sự kiện/đồ vật, không xác định A1 hay thời gian report A2.
- Giữ công thức A1 ∧ A2. Không đổi câu hỏi thành “ever deposited”, vì đó là đổi điều kiện rule.
- Trong test v1: 16 item chứa T chuẩn cũ, 3 item chứa T near cũ. Đây là số lần xuất hiện, **không phải số gold chắc chắn sai**.
- Quyết định: **sửa theo phương án trên**, người phê duyệt: **Kiệt** (phản hồi “xác nhận”). Câu sau triển khai và item sinh mới vẫn cần validate/audit.

### A02 — debt_limitation: phạm vi phủ định acknowledgment

- Nguồn: `rules.py:109-120`.
- Atom E1: có xác nhận nợ bằng văn bản trong khoảng từ due date đến filing date.
- Hiện tại F chuẩn: “never wrote to the creditor ...”, chỉ giới hạn một người nhận.
- Đề xuất F chuẩn: `Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.`
- Đề xuất F near: `Between the due date and the filing date, the debtor acknowledged the debt only orally in a phone call and made no written acknowledgment to anyone.`
- T chuẩn/near: giữ việc letter/email, nhưng kiểm date acknowledgment nằm trong interval ở **mọi** item sinh, không chỉ base. Các filing dates hiện tại đều sau 2019.
- Giữ mốc 1 March 2014 và filing dates hiện tại để tách kiểm số năm khỏi kiểm phủ định. Không đổi date để model dễ/khó hơn sau khi thấy output.
- Có 16 item test chứa F chuẩn cũ; không suy ra tất cả chúng sai gold vì atom khác có thể đủ kết luận.
- Quyết định: **sửa theo phương án trên**, người phê duyệt: **Kiệt** (phản hồi “xác nhận”). Câu sau triển khai và item sinh mới vẫn cần validate/audit.

### A03 — dismissal_no_notice: hợp đồng chuẩn có thể chứa protection

- Nguồn: `rules.py:165-183`.
- E1 = protection bằng written job-protection agreement do M ký.
- Hiện tại F chuẩn: không có written agreement ngoài standard contract; standard contract chưa rõ nội dung.
- Đề xuất F chuẩn: `W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.`
- Đề xuất F near: `M orally promised protection from dismissal without notice, but M signed no document providing that protection.`
- A1 F near hiện tại chỉ nói cãi nhau, không đụng/chống đối bằng đe dọa; chưa loại hết theft/fraud. Đề xuất: `W argued loudly with a customer, but committed no theft, violence or fraud.`
- Giữ A1 F chuẩn đã nêu “no theft, violence or fraud”. **Đính chính audit phụ:** câu chuẩn này có phủ định rõ; không được coi nó mơ hồ chỉ vì A2 bị bỏ. Nếu A1=F thì conjunction là F dù A2=U.
- Có 12 item test chứa E1 F chuẩn cũ; không gọi đây là 12 lỗi model/gold đã được xác minh.
- Quyết định: **sửa theo phương án trên**, người phê duyệt: **Kiệt** (phản hồi “xác nhận”). Câu sau triển khai và item sinh mới vẫn cần validate/audit.

### A04 — contract_breach: lịch sử tần suất không tương đương foreseeability

- Nguồn: `rules.py:144-160`.
- E1 = **sự kiện gây failure không thể dự liệu**, theo mốc thời gian cần định rõ trong rule/case mới.
- Đề xuất định nghĩa synthetic: “unforeseeable” được xác định tại lúc ký hợp đồng; không dùng tri thức luật ngoài prompt.
- Đề xuất T chuẩn: `At the time of contracting, the event that later prevented delivery could not reasonably have been foreseen by S.`
- Đề xuất T near: `A similar event had occurred elsewhere, but at the time of contracting this delivery-blocking event could not reasonably have been foreseen by S.`
- Đề xuất F chuẩn: `At the time of contracting, S could reasonably foresee the event that later prevented delivery.`
- Đề xuất F near: `The event was rare, but a specific warning available to S before contracting made it reasonably foreseeable.`
- Các câu sửa phải được kiểm độc lập; thêm “reasonably”/mốc contracting là **làm rõ quy ước mới**, không chứng minh gold cũ.
- Có 18 item chứa E1 T chuẩn, 3 chứa T near và 9 chứa F chuẩn. Các nhóm có thể khác nhau về atom đủ quyết định; không cộng thành số lỗi.
- Giới hạn: explicit foreseeable labels giảm nhu cầu diễn giải từ narrative. Chấp nhận để kiểm rule application; nếu muốn đo phân loại pháp lý từ facts, cần task/annotation riêng, không âm thầm trộn hai task.
- Quyết định: **sửa theo phương án trên**, người phê duyệt: **Kiệt** (phản hồi “xác nhận”). Câu sau triển khai và item sinh mới vẫn cần validate/audit.

### A05 — witnessed_contract: số người thực sự quan sát ký

- Nguồn: `rules.py:46-54`.
- Đề xuất rule mới: `The contract is valid exactly when at least two adults other than the parties watched both parties sign it.`
- Đề xuất F chuẩn: `No adult other than P and Q watched either party sign the contract.`
- Đề xuất F near: `Only one adult other than P and Q watched both parties sign. A second adult heard them from another room but did not see either party sign.`
- T chuẩn/near giữ hai adult observers, nói rõ cả hai không phải P/Q và xem cả hai bên ký.
- Đây là chốt “at least two”, người ký không tính witness, và hearing không tính watching. Không gán mặc định quy ước luật thật vào rule cũ.
- Quyết định: **sửa theo phương án trên**, người phê duyệt: **Kiệt** (phản hồi “xác nhận”). Câu sau triển khai và item sinh mới vẫn cần validate/audit.

## 2. Rà coverage toàn bộ 15 schema — không phải giấy chứng nhận pass

| Schema / split | Công thức hiện tại | Nội dung cần chốt trước dùng tiếp |
|---|---|---|
| refund_window / test | A1 | Chốt within 3 days gồm ngày thứ 3; return là physical return, không phải request. Chưa thấy thiếu liên kết rõ ở các ví dụ đã đọc. |
| noise_fine / dev | A1 | Chốt interval qua nửa đêm [22:00, 06:00] và tính cả hai biên. Một sự kiện noise duy nhất do R tạo. |
| witnessed_contract / test | A1 | A05; at least two, other than parties, actual visual observation. |
| tenancy_late / dev | A1 ∧ ¬E1 | Chốt written+signed và late strictly >30 days. Oral không tính written; kiểm cùng rent payment. |
| booking_cancel / test | A1 ∧ ¬E1 | Chốt thời điểm booking và calendar-day difference; hỏi quyền **full refund sau cancellation**, tránh “may cancel” trong khi V đã cancel. |
| minor_cancel / test | A1 ∧ ¬E1 | E1 có thể là consent cho đúng contract; e-mail tính written trong synthetic rule. `needs` làm thay đổi số câu khi flip age. |
| debt_limitation / test | A1 ∧ ¬E1 | A02; interval due→filing, no written acknowledgment to anyone; kiểm date theo lịch. |
| insurance_theft / dev | A1 ∧ ¬(E1 ∧ E2) | E2=possible reporting trong 48h phải xác định, không suy tự động từ illness/no phone. Near F “no coverage, reach station only after 3 days” chưa loại hết kênh report khác; nên nói không có phương tiện report nào trong khoảng đó. |
| contract_breach / test | A1 ∧ ¬(E1 ∧ E2) | A04; E1 cùng event với E2, same failure; định nghĩa foreseeability và kiểm facts không suy ngược sang atom khác ngoài ý định. |
| dismissal_no_notice / test | A1 ∧ A2 ∧ ¬E1 | A03; bảo vệ trong mọi document; near F misconduct phủ định đủ danh sách; deadline ngày lịch. |
| hotel_safe / test | A1 ∧ A2 | A01; watch identity, theft occurrence, safe position at theft. |
| licence_revocation / dev | A1 ∧ ¬E1 | Một violation cụ thể, notice cho violation đó; within 30 gồm ngày 30. Correction sentence có thể ngầm tiết lộ existence of violation khi A1 bị ẩn. |
| protected_tenant / dev | A1 ∧ ¬(E1 ∧ ¬E2) | Protected status và rent debt là facts độc lập về ngữ nghĩa; dependency E2→E1 trong generator không phải suy ra từ rule. Không để bảo vệ U bị hiểu là F. |
| severance_pay / dev | A1 ∧ A2 ∧ ¬(E1 ∨ E2) | Lý do position eliminated (A1 T chuẩn) có thể xung đột/đa lý do với gross-misconduct E1 T; tách A1 thành `The employer dismissed E.`. Không chỉ kiểm từng câu riêng. |
| defective_goods / dev | A1 ∧ A2 ∧ ¬E1 | F near “factory second” website nói nothing không loại seller thông báo bằng phone/email; bổ sung seller không thông báo bằng kênh nào. Chỉ rõ notice là notice đầu tiên; E1/A2 có thể tiết lộ defect khi A1 thiếu. |

Hướng xử lý trong bảng đã được **Kiệt xác nhận**. Những điểm còn cần cụ thể hóa (ví dụ context không tiết lộ atom U và item sau sinh) chưa được kiểm chứng chỉ bằng phê duyệt phương án. Với những hàng chưa thấy lỗi cụ thể, kết luận vẫn là “chưa thấy lỗi qua rà template”, không phải “gold đã đúng 100%”.

## 3. Quyết định về logic và sinh can thiệp

### B01 — Công thức ba giá trị

Giữ semantics Kleene hiện tại nếu được duyệt: T/F/U cho atom, thiếu atom là U; output theo công thức. Chốt cách đọc rule exceptions ở tầng logic trước khi so với natural language. Không dùng `X if C` thay cho biconditional nếu muốn kết luận no từ ¬C.

Checklist: phủ hết T/F/U assignments bằng bảng chân trị; verifier độc lập dùng định nghĩa truth table, không gọi lại cùng hàm `gold()` rồi coi đó là kiểm độc lập. Test v1 hiện chỉ kiểm một ví dụ conjunction/exception, chưa phủ toàn bộ truth tables.

### B02 — Không dùng missing facts để giả tạo U

Với mỗi base U, reviewer hoàn thành hai phép gán còn phù hợp với **toàn bộ text**: một cho yes, một cho no. Nếu không xây được cả hai, phải xem U có thực sự hợp lệ hay không. Ví dụ “reported the defect” có thể ngầm xác định defect; ghi rõ sự kiện nào được coi là stipulated, không bỏ A1 rồi giữ câu ngầm khẳng định nó mà vẫn claim A1 unknown.

### B03 — Can thiệp tối thiểu và dependencies

V1 `generate()` có thể flip một atom rồi drop các câu phụ thuộc (`v1.py:111-118`). Không tiếp tục gọi mọi pair đó là one-fact minimal intervention.

Đề xuất: chỉ nhận pair thay đúng **một factual proposition** và không đổi/trút bỏ propositions khác. Nếu coherence bắt buộc phải sửa thêm, gắn `compound/context-repair`, tách khỏi headline one-fact; hoặc thiết kế lại context cho các atoms độc lập. Không chọn giải pháp chỉ vì tạo nhiều item hơn.

### B04 — Trùng prompt

V1 có 239 ID test / 183 unique prompts. Đề xuất tách:
- Unit accuracy: một stimulus một trọng số, aggregation được chốt trước.
- Pair/edge behavior: mỗi edge base→intervention có provenance, trọng số theo schema; không giả vờ stimuli độc lập.

Không dedupe hồi tố để thay headline v1. Tất cả đây là lựa chọn protocol mới chưa triển khai.

### B05 — M5

Không gọi current M5 là explanation alignment đã xác lập. Đề xuất **tạm bỏ M5 khỏi kết luận năng lực**, giữ raw explanations cho qualitative audit. Chỉ thêm lại khi có gold support sets (có thể nhiều fact), quy tắc answer-conditioned/unconditional, format validity báo riêng, và quy tắc unknown rõ. Không sửa parser để ưu ái model sau khi xem test.

## 4. Điều kiện dừng trước API run kế tiếp

- [x] Kiệt xác nhận phương án A01–A05 và hướng xử lý coverage 15 schemas.
- [ ] Triển khai phương án và kiểm toàn bộ item mới; không còn cờ facts↔atoms chưa quyết.
- [ ] Người thứ hai kiểm mẫu theo protocol và ghi quyết định; nếu chưa có, báo **chưa kiểm chứng**, không giả completion.
- [ ] Quy tắc thresholds/time/written/negation và truth tables được chốt; no missing-premise shortcuts.
- [ ] One-proposition edits, dependency/context repair và duplicate weighting được chốt.
- [ ] Metric headline không đổi theo thứ hạng mong muốn; M5 chỉ đưa lại khi có gold support.
- [ ] Model-independent checks qua; freeze items, prompts, code snapshot và request metadata trước run.
- [ ] Có held-out schema mới: test v1 đã xem output không còn là unseen test cho v2.

**Đã hoàn thành:** phiếu adjudication và phê duyệt phương án bởi Kiệt. **Chưa làm:** kiểm người thứ hai, triển khai/validate dataset mới, build/run v2, cập nhật midterm, commit hoặc push. Phê duyệt phương án không tự cho phép ghi đè v1, chạy API mới hay push.
