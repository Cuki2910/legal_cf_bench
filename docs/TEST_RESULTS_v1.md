# Test results v1 (frozen test split, 8 schemas, 239 items)
CI = cluster bootstrap over schemas (8 clusters), wide by construction. Gold computed from formula; not expert-checked ("chưa kiểm chứng").

## Trạng thái và giới hạn diễn giải

- Đã kiểm tra lại từ raw: cả 6 run đều có đủ 239 ID duy nhất, không thiếu/thừa item, không khác kết quả parser đang dùng. Tổng cộng 1.434 phản hồi. Không gọi lại API trong lần kiểm tra này.
- Regression suite offline: 9 test qua (`python3 -W error::ResourceWarning -m unittest discover -s legal_cf_bench/tests`, chạy từ UROP).
- SHA-256 của tập test hiện tại khớp `TEST_FREEZE.txt`: `5a3e55ce1ef6db40db2829e67abfc1dac0748f235fd33d4deb6610e288eb7e2e`. Hash này bao phủ JSON item sinh ra, không bao phủ toàn bộ mã parser/scoring/prompt; không thay thế một code snapshot có version.
- Đây là **điểm khớp gold của benchmark tổng hợp chưa được audit đầy đủ**, không phải xếp hạng năng lực pháp lý. Công thức tính đúng không bảo đảm câu tiếng Anh biểu đạt đúng phép gán atom.
- Audit 100% item bởi Kiệt và kiểm tra người thứ hai chưa được xác nhận trước khi chạy; đây là bước kiểm soát chất lượng còn thiếu, không được xem là đã hoàn tất chỉ vì Kiệt duyệt chạy.
- pA và pB là hai prompt khác nhau, **không phải hai lần lặp cùng cấu hình**. Chưa ước lượng được tính không tất định của gateway.
- Haiku pA có 1 phản hồi không parse được: `dismissal_no_notice/yes/N.A2`; raw kết thúc giữa câu (1.013 ký tự). Chưa lưu `finish_reason` nên chưa xác nhận nguyên nhân cắt. Giữ nguyên và tính là không đúng; không retry riêng item để chọn kết quả khác.
- Các CI chênh lệch gộp mọi loại can thiệp bên dưới là **phân tích bổ sung/exploratory**, không phải headline đã khai báo trước. Không hiệu chỉnh nhiều phép so sánh; CI chỉ resample 8 schema và không chứa bất định do gold sai/mơ hồ.
- Model IDs là nhãn route gateway; chưa xác minh độc lập model thực tế phía sau route. Các record chỉ lưu `id`, `answer`, `deciding_fact`, `raw`; không có provider response envelope, usage, finish_reason hay bản sao prompt cho từng request. Vì vậy không thể kiểm chứng hậu nghiệm model identity, mức cắt output hay prompt biến đổi ở gateway từ các raw này.
- Không sửa test/gold hoặc chọn bỏ item sau khi xem điểm. Mọi lỗi thiết kế phát hiện sau chạy phải được gắn cờ riêng; sửa chúng thuộc phiên bản benchmark mới.
- Chưa chèn điểm test vào báo cáo midterm, chưa commit/push. Trước khi dùng như kết quả nghiên cứu, cần hoàn tất audit ngữ nghĩa facts↔atoms, phân loại bất đồng gold/model và xác định giao thức phiên bản kế tiếp.

### Headline theo gold hiện tại (không điều kiện, pA / pB)

| Model | M1 flip | M2 near-miss | M3(I1) irrelevant plausible |
|---|---|---|---|
| Sol | 61/80 / 64/80 | 27/39 / 27/39 | 38/48 / 39/48 |
| Luna | 65/80 / 65/80 | 31/39 / 29/39 | 40/48 / 40/48 |
| Haiku 4.5 | 70/80 / 69/80 | 32/39 / 35/39 | 43/48 / 44/48 |

Haiku có điểm khớp gold cao hơn ở cả ba headline trong hai prompt; điều này chưa chứng minh Haiku có năng lực tốt hơn. Đặc biệt, ở pA cả 58 bất đồng Sol–gold đều là gold yes/no nhưng Sol trả `undetermined`; cần audit xem facts có thật sự xác định đáp án hay không trước khi gọi chúng là lỗi model.

### Paired cluster bootstrap cho từng headline (bổ sung, pooled pA+pB)

Resample theo schema, giữ hai prompt trong cùng cluster; 2.000 lần, seed 0. Chênh lệch theo thang tỷ lệ, CI percentile 95%; chưa hiệu chỉnh nhiều phép so sánh.

| Chênh lệch | M1 | M2 | M3(I1) |
|---|---|---|---|
| Haiku − Sol | +0.0875 [−0.0197, +0.1842] | +0.1667 [+0.0341, +0.2941] | +0.1042 [−0.0208, +0.2188] |
| Luna − Sol | +0.0312 [+0.0054, +0.0809] | +0.0769 [−0.0161, +0.1977] | +0.0312 [−0.0208, +0.0833] |

Các khoảng không chứa 0 chỉ mô tả khác biệt **so với gold hiện tại**, không giải quyết tính hợp lệ của gold.

### Sai lệch triển khai cần giữ khi diễn giải

- Quy mô thực tế: 15 schema (7 dev + 8 test), 474 item/prompt tổng cộng; test có 24 base + 215 can thiệp. Đây là bản mở rộng so với đề xuất ban đầu 12 schema.
- M2 trong mã gộp `N1/N2` thành `N`; `N3` được dùng cho flip có cách diễn đạt gần ngưỡng/near-text, không bảo đảm luôn là boundary số. Không diễn giải riêng hiệu ứng numerical-boundary từ nhãn này.
- `position=end/middle` được áp dụng cho I1/I2; các can thiệp atom ở slot của template. Chưa phải thiết kế vị trí đầy đủ cho mọi loại can thiệp.
- M5 hiện chỉ kiểm tra model có chỉ vào **fact bị can thiệp** trên flip trả lời đúng và gold mới xác định hay không. Nó không chấm tất cả tập tình tiết đủ để quyết định, không đo explanation faithfulness, và mẫu số giữa model khác nhau. Vì vậy chỉ báo cáo như proxy phụ.
- M1 không điều kiện ở đây là **độ đúng của đáp án sau can thiệp**, không trực tiếp đòi model đổi đáp án so với chính đáp án base của nó. Bản có điều kiện chỉ xét base đúng; với gold đổi, đáp án mới đúng khi đó đồng thời bảo đảm đổi đáp án. M2/M3 không điều kiện cũng là độ đúng so với gold, không chỉ là giữ nguyên đáp án model. Không tráo các nghĩa này khi diễn giải.
- Oracle kiểm tra tính nhất quán pipeline theo gold, không xác minh gold tiếng Anh đúng về mặt ngữ nghĩa/pháp lý.

### Kết luận tạm thời

Đã hoàn thành chạy, kiểm tra tính toàn vẹn và audit kỹ thuật bằng trợ lý: **chưa xác lập benchmark hợp lệ để xếp hạng model**. Audit phát hiện facts chưa xác định atom ở `hotel_safe`, `debt_limitation`, `dismissal_no_notice`, `contract_breach`; 239 ID tương ứng 183 prompt duy nhất (46 nhóm trùng chứa 102 item). M5 còn trộn việc chọn fact bị sửa với tuân thủ format một ID. Xem [TEST_VALIDITY_AUDIT_v1.md](TEST_VALIDITY_AUDIT_v1.md) để biết bằng chứng và giới hạn. Không thay gold/raw/điểm sau audit; không coi mọi `undetermined` của Sol là lỗi, cũng không suy ra mọi điểm Haiku cao hơn là do gold. Audit này không thay thế Kiệt/người thứ hai xác minh gold.

### Provenance dữ liệu cục bộ

Nguồn trực tiếp cho mọi số trong báo cáo (không phải số liệu lấy từ paper/web):

- `../results/v1__openai-cx_gpt-6.1-sol__test_pA/raw.jsonl`
- `../results/v1__openai-cx_gpt-6.1-sol__test_pB/raw.jsonl`
- `../results/v1__openai-cx_gpt-6-luna_1m___test_pA/raw.jsonl`
- `../results/v1__openai-cx_gpt-6-luna_1m___test_pB/raw.jsonl`
- `../results/v1__openai-cc_claude-haiku-4-5-20251001__test_pA/raw.jsonl`
- `../results/v1__openai-cc_claude-haiku-4-5-20251001__test_pB/raw.jsonl`
- Gold/template: `../lcb/rules.py`; sinh item, parser, score: `../lcb/v1.py`; freeze: `TEST_FREEZE.txt`.

## Prompt pA
**sol** n=239 unparsable=0
- M0 base: 0.708 (17/24) CI(0.583, 0.833)
- M1_flip_sensitivity: uncond 0.762 (61/80) CI(0.632, 0.875) | cond 0.731 (38/52) CI(0.55, 0.87)
- M2_nearmiss_specificity: uncond 0.692 (27/39) CI(0.488, 0.889) | cond 1.0 (23/23) CI(1.0, 1.0)
- M3a_irrelevant_plausible: uncond 0.792 (38/48) CI(0.625, 0.917) | cond 1.0 (34/34) CI(1.0, 1.0)
- M3b_irrelevant_lexical: uncond 0.792 (38/48) CI(0.625, 0.917) | cond 1.0 (34/34) CI(1.0, 1.0)
- M4 case consistency: 0.333 (8/24) CI(0.083, 0.625)
- M5 deciding-fact agreement: 0.983 (58/59) CI(0.952, 1.0)
- M7: lip_from_yes 25/30; flip_from_no 13/18; undetermined 23/32
- by tier M1: T1 9/12; T2 27/30; T3 18/28; T4 7/10
- by tier M2: T1 3/4; T2 14/15; T3 7/15; T4 3/5
- by kind: F 26/32; I1 38/48; I2 38/48; N 27/39; N3 25/32; S 10/16; base 17/24
- by schema: refund_window 23/23; witnessed_contract 18/23; booking_cancel 28/30; minor_cancel 30/30; debt_limitation 22/30; contract_breach 14/37; dismissal_no_notice 26/36; hotel_safe 20/30
**luna** n=239 unparsable=0
- M0 base: 0.833 (20/24) CI(0.708, 0.958)
- M1_flip_sensitivity: uncond 0.812 (65/80) CI(0.69, 0.944) | cond 0.823 (51/62) CI(0.69, 0.944)
- M2_nearmiss_specificity: uncond 0.795 (31/39) CI(0.66, 0.941) | cond 0.966 (28/29) CI(0.903, 1.0)
- M3a_irrelevant_plausible: uncond 0.833 (40/48) CI(0.708, 0.938) | cond 0.95 (38/40) CI(0.875, 1.0)
- M3b_irrelevant_lexical: uncond 0.875 (42/48) CI(0.771, 0.958) | cond 1.0 (40/40) CI(1.0, 1.0)
- M4 case consistency: 0.5 (12/24) CI(0.208, 0.792)
- M5 deciding-fact agreement: 0.921 (58/63) CI(0.855, 0.983)
- M7: lip_from_yes 27/30; flip_from_no 12/18; undetermined 26/32
- by tier M1: T1 12/12; T2 28/30; T3 18/28; T4 7/10
- by tier M2: T1 4/4; T2 14/15; T3 9/15; T4 4/5
- by kind: F 27/32; I1 40/48; I2 42/48; N 31/39; N3 26/32; S 12/16; base 20/24
- by schema: refund_window 23/23; witnessed_contract 22/23; booking_cancel 30/30; minor_cancel 30/30; debt_limitation 24/30; contract_breach 20/37; dismissal_no_notice 26/36; hotel_safe 23/30
**haiku** n=239 unparsable=1
- M0 base: 0.875 (21/24) CI(0.708, 1.0)
- M1_flip_sensitivity: uncond 0.875 (70/80) CI(0.75, 0.988) | cond 0.9 (63/70) CI(0.778, 0.988)
- M2_nearmiss_specificity: uncond 0.821 (32/39) CI(0.679, 0.971) | cond 0.906 (29/32) CI(0.806, 1.0)
- M3a_irrelevant_plausible: uncond 0.896 (43/48) CI(0.75, 1.0) | cond 1.0 (42/42) CI(1.0, 1.0)
- M3b_irrelevant_lexical: uncond 0.896 (43/48) CI(0.771, 0.979) | cond 0.976 (41/42) CI(0.925, 1.0)
- M4 case consistency: 0.625 (15/24) CI(0.375, 0.833)
- M5 deciding-fact agreement: 0.853 (58/68) CI(0.758, 0.946)
- M7: lip_from_yes 27/30; flip_from_no 16/18; undetermined 27/32
- by tier M1: T1 12/12; T2 25/30; T3 23/28; T4 10/10
- by tier M2: T1 4/4; T2 14/15; T3 9/15; T4 5/5
- by kind: F 28/32; I1 43/48; I2 43/48; N 32/39; N3 28/32; S 14/16; base 21/24
- by schema: refund_window 23/23; witnessed_contract 19/23; booking_cancel 30/30; minor_cancel 28/30; debt_limitation 26/30; contract_breach 20/37; dismissal_no_notice 33/36; hotel_safe 30/30
## Prompt pB
**sol** n=239 unparsable=0
- M0 base: 0.792 (19/24) CI(0.625, 0.917)
- M1_flip_sensitivity: uncond 0.8 (64/80) CI(0.677, 0.922) | cond 0.81 (47/58) CI(0.667, 0.929)
- M2_nearmiss_specificity: uncond 0.692 (27/39) CI(0.488, 0.889) | cond 0.962 (25/26) CI(0.85, 1.0)
- M3a_irrelevant_plausible: uncond 0.812 (39/48) CI(0.688, 0.938) | cond 1.0 (38/38) CI(1.0, 1.0)
- M3b_irrelevant_lexical: uncond 0.812 (39/48) CI(0.688, 0.938) | cond 1.0 (38/38) CI(1.0, 1.0)
- M4 case consistency: 0.458 (11/24) CI(0.167, 0.75)
- M5 deciding-fact agreement: 0.952 (59/62) CI(0.896, 1.0)
- M7: lip_from_yes 26/30; flip_from_no 13/18; undetermined 25/32
- by tier M1: T1 11/12; T2 28/30; T3 18/28; T4 7/10
- by tier M2: T1 3/4; T2 14/15; T3 7/15; T4 3/5
- by kind: F 27/32; I1 39/48; I2 39/48; N 27/39; N3 25/32; S 12/16; base 19/24
- by schema: refund_window 23/23; witnessed_contract 21/23; booking_cancel 30/30; minor_cancel 30/30; debt_limitation 22/30; contract_breach 16/37; dismissal_no_notice 26/36; hotel_safe 20/30
**luna** n=239 unparsable=0
- M0 base: 0.833 (20/24) CI(0.708, 0.958)
- M1_flip_sensitivity: uncond 0.812 (65/80) CI(0.707, 0.922) | cond 0.79 (49/62) CI(0.643, 0.922)
- M2_nearmiss_specificity: uncond 0.744 (29/39) CI(0.659, 0.85) | cond 0.931 (27/29) CI(0.828, 1.0)
- M3a_irrelevant_plausible: uncond 0.833 (40/48) CI(0.708, 0.958) | cond 1.0 (40/40) CI(1.0, 1.0)
- M3b_irrelevant_lexical: uncond 0.833 (40/48) CI(0.708, 0.958) | cond 1.0 (40/40) CI(1.0, 1.0)
- M4 case consistency: 0.417 (10/24) CI(0.167, 0.667)
- M5 deciding-fact agreement: 0.794 (50/63) CI(0.648, 0.938)
- M7: lip_from_yes 26/30; flip_from_no 14/18; undetermined 25/32
- by tier M1: T1 11/12; T2 28/30; T3 19/28; T4 7/10
- by tier M2: T1 3/4; T2 13/15; T3 10/15; T4 3/5
- by kind: F 27/32; I1 40/48; I2 40/48; N 29/39; N3 26/32; S 12/16; base 20/24
- by schema: refund_window 23/23; witnessed_contract 21/23; booking_cancel 29/30; minor_cancel 30/30; debt_limitation 22/30; contract_breach 23/37; dismissal_no_notice 26/36; hotel_safe 20/30
**haiku** n=239 unparsable=0
- M0 base: 0.958 (23/24) CI(0.875, 1.0)
- M1_flip_sensitivity: uncond 0.863 (69/80) CI(0.795, 0.941) | cond 0.855 (65/76) CI(0.776, 0.941)
- M2_nearmiss_specificity: uncond 0.897 (35/39) CI(0.826, 0.973) | cond 0.944 (34/36) CI(0.889, 1.0)
- M3a_irrelevant_plausible: uncond 0.917 (44/48) CI(0.792, 1.0) | cond 0.957 (44/46) CI(0.905, 1.0)
- M3b_irrelevant_lexical: uncond 0.938 (45/48) CI(0.854, 1.0) | cond 0.978 (45/46) CI(0.935, 1.0)
- M4 case consistency: 0.583 (14/24) CI(0.333, 0.833)
- M5 deciding-fact agreement: 0.866 (58/67) CI(0.797, 0.929)
- M7: lip_from_yes 27/30; flip_from_no 14/18; undetermined 28/32
- by tier M1: T1 12/12; T2 25/30; T3 24/28; T4 8/10
- by tier M2: T1 4/4; T2 15/15; T3 12/15; T4 4/5
- by kind: F 27/32; I1 44/48; I2 45/48; N 35/39; N3 28/32; S 14/16; base 23/24
- by schema: refund_window 23/23; witnessed_contract 23/23; booking_cancel 28/30; minor_cancel 30/30; debt_limitation 27/30; contract_breach 26/37; dismissal_no_notice 34/36; hotel_safe 25/30

## M6 prompt stability (same answer under pA and pB)
- sol: 0.971 (232/239) CI(0.939, 0.992)
- luna: 0.925 (221/239) CI(0.873, 0.976)
- haiku: 0.87 (208/239) CI(0.79, 0.938)

## Paired difference in accuracy over all non-base items (pA and pB pooled), cluster bootstrap by schema, 95%
- sol - haiku: pooled (-0.112, (-0.18, -0.032)) | pA (-0.112, (-0.191, -0.026)) | pB (-0.112, (-0.187, -0.025))
- sol - luna: pooled (-0.044, (-0.092, -0.007)) | pA (-0.065, (-0.111, -0.023)) | pB (-0.023, (-0.079, 0.014))
- luna - haiku: pooled (-0.067, (-0.126, -0.007)) | pA (-0.047, (-0.116, 0.026)) | pB (-0.088, (-0.145, -0.028))

## Model-free baselines on test split
- const-yes: M0 0.333 M1 0.325 M2 0.41 M3a 0.333 M3b 0.333
- const-no: M0 0.333 M1 0.65 M2 0.385 M3a 0.333 M3b 0.333
- const-undetermined: M0 0.333 M1 0.025 M2 0.205 M3a 0.333 M3b 0.333
- keyword-trigger: M0 1.0 M1 0.775 M2 0.154 M3a 0.375 M3b 0.375
- oracle: M0 1.0 M1 1.0 M2 1.0 M3a 1.0 M3b 1.0

## Error summary (which gold -> which answer), pA
- sol: yes->undetermined 40; no->undetermined 18
- luna: yes->undetermined 22; no->undetermined 15; yes->no 4
- haiku: no->undetermined 14; yes->undetermined 9; yes->no 4; no->yes 2; yes->None 1
