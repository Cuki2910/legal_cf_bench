# Items v1 (generated; gold computed from formula). Kiet: mark any item whose gold you dispute.


## refund_window (tier 1, test)
RULE: A shop must refund a returned item if and only if the item is returned within 3 days of purchase.
Q: Must the shop refund the item?

**refund_window/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 2 days after buying it.

**refund_window/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 10 days after buying it.

**refund_window/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C first contacted the shop about a return 2 days after buying the jacket, but brought the jacket back 6 days after buying it.

**refund_window/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket 1 day after buying it, after wearing it once.

**refund_window/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 2 days after buying it.
  F3. The jacket was sold at a discount of 30 percent.

**refund_window/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Customer C bought a jacket from a shop.
  F2. The jacket was sold at a discount of 30 percent.
  F3. C returned the jacket to the shop 2 days after buying it.

**refund_window/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 2 days after buying it.
  F3. The shop is located on the second floor of a mall.

**refund_window/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Customer C bought a jacket from a shop.
  F2. The shop is located on the second floor of a mall.
  F3. C returned the jacket to the shop 2 days after buying it.

**refund_window/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 10 days after buying it.

**refund_window/no/F.A1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 2 days after buying it.

**refund_window/no/N3.A1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket 1 day after buying it, after wearing it once.

**refund_window/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C first contacted the shop about a return 2 days after buying the jacket, but brought the jacket back 6 days after buying it.

**refund_window/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 10 days after buying it.
  F3. The jacket was sold at a discount of 30 percent.

**refund_window/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Customer C bought a jacket from a shop.
  F2. The jacket was sold at a discount of 30 percent.
  F3. C returned the jacket to the shop 10 days after buying it.

**refund_window/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 10 days after buying it.
  F3. The shop is located on the second floor of a mall.

**refund_window/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Customer C bought a jacket from a shop.
  F2. The shop is located on the second floor of a mall.
  F3. C returned the jacket to the shop 10 days after buying it.

**refund_window/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Customer C bought a jacket from a shop.

**refund_window/undetermined/S.A1T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 2 days after buying it.

**refund_window/undetermined/S.A1F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Customer C bought a jacket from a shop.
  F2. C returned the jacket to the shop 10 days after buying it.

**refund_window/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Customer C bought a jacket from a shop.
  F2. The jacket was sold at a discount of 30 percent.

**refund_window/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Customer C bought a jacket from a shop.
  F2. The jacket was sold at a discount of 30 percent.

**refund_window/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Customer C bought a jacket from a shop.
  F2. The shop is located on the second floor of a mall.

**refund_window/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Customer C bought a jacket from a shop.
  F2. The shop is located on the second floor of a mall.

## noise_fine (tier 1, dev)
RULE: A resident must pay a noise fine if and only if the noise was made between 22:00 and 06:00.
Q: Must the resident pay a noise fine?

**noise_fine/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 23:30.

**noise_fine/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 15:00.

**noise_fine/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 21:50.

**noise_fine/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 05:45, shortly before sunrise.

**noise_fine/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 23:30.
  F3. R had received a written warning about noise one year earlier.

**noise_fine/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R had received a written warning about noise one year earlier.
  F3. R played the loud music at 23:30.

**noise_fine/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 23:30.
  F3. R's flat is on the fourth floor.

**noise_fine/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R's flat is on the fourth floor.
  F3. R played the loud music at 23:30.

**noise_fine/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 15:00.

**noise_fine/no/F.A1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 23:30.

**noise_fine/no/N3.A1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 05:45, shortly before sunrise.

**noise_fine/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 21:50.

**noise_fine/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 15:00.
  F3. R had received a written warning about noise one year earlier.

**noise_fine/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R had received a written warning about noise one year earlier.
  F3. R played the loud music at 15:00.

**noise_fine/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 15:00.
  F3. R's flat is on the fourth floor.

**noise_fine/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R's flat is on the fourth floor.
  F3. R played the loud music at 15:00.

**noise_fine/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.

**noise_fine/undetermined/S.A1T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 23:30.

**noise_fine/undetermined/S.A1F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R played the loud music at 15:00.

**noise_fine/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R had received a written warning about noise one year earlier.

**noise_fine/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R had received a written warning about noise one year earlier.

**noise_fine/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R's flat is on the fourth floor.

**noise_fine/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Resident R played loud music in R's flat and a neighbour complained.
  F2. R's flat is on the fourth floor.

## witnessed_contract (tier 1, test)
RULE: A contract is valid if and only if two adult witnesses watched the parties sign it.
Q: Is the contract valid?

**witnessed_contract/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract.

**witnessed_contract/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Nobody other than P and Q was present when they signed the contract.

**witnessed_contract/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. One adult witness watched P and Q sign the contract, and a second adult was in the next room and could hear them.

**witnessed_contract/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract; one of the witnesses was P's cousin.

**witnessed_contract/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract.
  F3. The contract price was 200 dollars.

**witnessed_contract/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract price was 200 dollars.
  F3. Two adult witnesses watched P and Q sign the contract.

**witnessed_contract/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract.
  F3. The contract was written in blue ink.

**witnessed_contract/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract was written in blue ink.
  F3. Two adult witnesses watched P and Q sign the contract.

**witnessed_contract/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Nobody other than P and Q was present when they signed the contract.

**witnessed_contract/no/F.A1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract.

**witnessed_contract/no/N3.A1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract; one of the witnesses was P's cousin.

**witnessed_contract/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. One adult witness watched P and Q sign the contract, and a second adult was in the next room and could hear them.

**witnessed_contract/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Nobody other than P and Q was present when they signed the contract.
  F3. The contract price was 200 dollars.

**witnessed_contract/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract price was 200 dollars.
  F3. Nobody other than P and Q was present when they signed the contract.

**witnessed_contract/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Nobody other than P and Q was present when they signed the contract.
  F3. The contract was written in blue ink.

**witnessed_contract/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract was written in blue ink.
  F3. Nobody other than P and Q was present when they signed the contract.

**witnessed_contract/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.

**witnessed_contract/undetermined/S.A1T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Two adult witnesses watched P and Q sign the contract.

**witnessed_contract/undetermined/S.A1F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. Nobody other than P and Q was present when they signed the contract.

**witnessed_contract/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract price was 200 dollars.

**witnessed_contract/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract price was 200 dollars.

**witnessed_contract/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract was written in blue ink.

**witnessed_contract/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Parties P and Q signed a contract to sell a bicycle.
  F2. The contract was written in blue ink.

## tenancy_late (tier 2, dev)
RULE: A landlord may evict a tenant if and only if the tenant paid rent more than 30 days late, unless the landlord accepted the late payment in a signed written notice.
Q: May the landlord evict the tenant?

**tenancy_late/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L never signed any written notice about the late payment.

**tenancy_late/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 12 days late.
  F3. L never signed any written notice about the late payment.

**tenancy_late/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent exactly 30 days late.
  F3. L never signed any written notice about the late payment.

**tenancy_late/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 31 days late.
  F3. L never signed any written notice about the late payment.

**tenancy_late/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice accepting T's late payment.

**tenancy_late/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice that began by complaining about the delay but ended with the words 'I accept the late payment.'

**tenancy_late/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L told T by phone that the late payment was acceptable, but never put it in writing.

**tenancy_late/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L never signed any written notice about the late payment.
  F4. T had paid every earlier month's rent on time for five years.

**tenancy_late/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Landlord L rents a flat to tenant T.
  F2. T had paid every earlier month's rent on time for five years.
  F3. T paid the monthly rent 45 days late.
  F4. L never signed any written notice about the late payment.

**tenancy_late/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L never signed any written notice about the late payment.
  F4. T's flat is on the fifth floor.

**tenancy_late/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Landlord L rents a flat to tenant T.
  F2. T's flat is on the fifth floor.
  F3. T paid the monthly rent 45 days late.
  F4. L never signed any written notice about the late payment.

**tenancy_late/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice accepting T's late payment.

**tenancy_late/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 31 days late.
  F3. L signed a written notice accepting T's late payment.

**tenancy_late/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L never signed any written notice about the late payment.

**tenancy_late/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L told T by phone that the late payment was acceptable, but never put it in writing.

**tenancy_late/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice that began by complaining about the delay but ended with the words 'I accept the late payment.'

**tenancy_late/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice accepting T's late payment.
  F4. T had paid every earlier month's rent on time for five years.

**tenancy_late/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Landlord L rents a flat to tenant T.
  F2. T had paid every earlier month's rent on time for five years.
  F3. T paid the monthly rent 45 days late.
  F4. L signed a written notice accepting T's late payment.

**tenancy_late/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice accepting T's late payment.
  F4. T's flat is on the fifth floor.

**tenancy_late/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Landlord L rents a flat to tenant T.
  F2. T's flat is on the fifth floor.
  F3. T paid the monthly rent 45 days late.
  F4. L signed a written notice accepting T's late payment.

**tenancy_late/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.

**tenancy_late/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 12 days late.

**tenancy_late/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent exactly 30 days late.

**tenancy_late/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 31 days late.

**tenancy_late/undetermined/S.E1T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L signed a written notice accepting T's late payment.

**tenancy_late/undetermined/S.E1F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. L never signed any written notice about the late payment.

**tenancy_late/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. T had paid every earlier month's rent on time for five years.

**tenancy_late/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Landlord L rents a flat to tenant T.
  F2. T had paid every earlier month's rent on time for five years.
  F3. T paid the monthly rent 45 days late.

**tenancy_late/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Landlord L rents a flat to tenant T.
  F2. T paid the monthly rent 45 days late.
  F3. T's flat is on the fifth floor.

**tenancy_late/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Landlord L rents a flat to tenant T.
  F2. T's flat is on the fifth floor.
  F3. T paid the monthly rent 45 days late.

## booking_cancel (tier 2, test)
RULE: A traveller may cancel a hotel booking for a full refund if and only if the traveller cancelled at least 7 days before check-in, unless the booking was marked non-refundable at the time of booking.
Q: May the traveller cancel the booking for a full refund?

**booking_cancel/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 17 June.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 14 June, 6 days before check-in.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 13 June, exactly 7 days before check-in.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking confirmation stated 'non-refundable' at the time of booking.

**booking_cancel/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking page showed 'non-refundable' in the small print under the price, and V ticked the box accepting the terms.

**booking_cancel/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The hotel's website marked the room rate as non-refundable, but V's booking, made through a travel agent, was marked refundable at the time of booking.

**booking_cancel/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking was marked fully refundable at the time of booking.
  F4. V had stayed at the same hotel twice before.

**booking_cancel/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V had stayed at the same hotel twice before.
  F3. V cancelled the booking on 8 June.
  F4. The booking was marked fully refundable at the time of booking.

**booking_cancel/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking was marked fully refundable at the time of booking.
  F4. The hotel room had a view of the sea.

**booking_cancel/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The hotel room had a view of the sea.
  F3. V cancelled the booking on 8 June.
  F4. The booking was marked fully refundable at the time of booking.

**booking_cancel/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking confirmation stated 'non-refundable' at the time of booking.

**booking_cancel/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 13 June, exactly 7 days before check-in.
  F3. The booking confirmation stated 'non-refundable' at the time of booking.

**booking_cancel/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The hotel's website marked the room rate as non-refundable, but V's booking, made through a travel agent, was marked refundable at the time of booking.

**booking_cancel/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking page showed 'non-refundable' in the small print under the price, and V ticked the box accepting the terms.

**booking_cancel/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking confirmation stated 'non-refundable' at the time of booking.
  F4. V had stayed at the same hotel twice before.

**booking_cancel/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V had stayed at the same hotel twice before.
  F3. V cancelled the booking on 8 June.
  F4. The booking confirmation stated 'non-refundable' at the time of booking.

**booking_cancel/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking confirmation stated 'non-refundable' at the time of booking.
  F4. The hotel room had a view of the sea.

**booking_cancel/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The hotel room had a view of the sea.
  F3. V cancelled the booking on 8 June.
  F4. The booking confirmation stated 'non-refundable' at the time of booking.

**booking_cancel/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The booking was marked fully refundable at the time of booking.

**booking_cancel/undetermined/S.A1T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 8 June.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/undetermined/S.A1F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V cancelled the booking on 17 June.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/undetermined/F.E1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The booking confirmation stated 'non-refundable' at the time of booking.

**booking_cancel/undetermined/N3.E1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The booking page showed 'non-refundable' in the small print under the price, and V ticked the box accepting the terms.

**booking_cancel/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The hotel's website marked the room rate as non-refundable, but V's booking, made through a travel agent, was marked refundable at the time of booking.

**booking_cancel/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The booking was marked fully refundable at the time of booking.
  F3. V had stayed at the same hotel twice before.

**booking_cancel/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. V had stayed at the same hotel twice before.
  F3. The booking was marked fully refundable at the time of booking.

**booking_cancel/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The booking was marked fully refundable at the time of booking.
  F3. The hotel room had a view of the sea.

**booking_cancel/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Traveller V booked a hotel room for a stay beginning on 20 June.
  F2. The hotel room had a view of the sea.
  F3. The booking was marked fully refundable at the time of booking.

## minor_cancel (tier 2, test)
RULE: A signer may cancel a contract if and only if the signer was under 18 when signing it, unless the signer's guardian consented to the contract in writing.
Q: May Z cancel the contract?

**minor_cancel/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian never gave any consent to the contract, written or oral.

**minor_cancel/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 25 years old when signing the contract.

**minor_cancel/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z turned 18 one day before signing the contract.

**minor_cancel/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 17 years and 11 months old when signing the contract.
  F3. Z's guardian never gave any consent to the contract, written or oral.

**minor_cancel/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's mother, who is Z's legal guardian, signed a written consent to the contract.

**minor_cancel/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian wrote a short e-mail to the shop saying 'Z may buy the laptop'.

**minor_cancel/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian told Z orally 'go ahead and buy the laptop' but gave no written consent.

**minor_cancel/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian never gave any consent to the contract, written or oral.
  F4. Z's guardian is a lawyer.

**minor_cancel/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z's guardian is a lawyer.
  F3. Z was 16 years old when signing the contract.
  F4. Z's guardian never gave any consent to the contract, written or oral.

**minor_cancel/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian never gave any consent to the contract, written or oral.
  F4. The laptop is silver.

**minor_cancel/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. The laptop is silver.
  F3. Z was 16 years old when signing the contract.
  F4. Z's guardian never gave any consent to the contract, written or oral.

**minor_cancel/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's mother, who is Z's legal guardian, signed a written consent to the contract.

**minor_cancel/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 17 years and 11 months old when signing the contract.
  F3. Z's mother, who is Z's legal guardian, signed a written consent to the contract.

**minor_cancel/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian never gave any consent to the contract, written or oral.

**minor_cancel/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian told Z orally 'go ahead and buy the laptop' but gave no written consent.

**minor_cancel/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian wrote a short e-mail to the shop saying 'Z may buy the laptop'.

**minor_cancel/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's mother, who is Z's legal guardian, signed a written consent to the contract.
  F4. Z's guardian is a lawyer.

**minor_cancel/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z's guardian is a lawyer.
  F3. Z was 16 years old when signing the contract.
  F4. Z's mother, who is Z's legal guardian, signed a written consent to the contract.

**minor_cancel/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's mother, who is Z's legal guardian, signed a written consent to the contract.
  F4. The laptop is silver.

**minor_cancel/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. The laptop is silver.
  F3. Z was 16 years old when signing the contract.
  F4. Z's mother, who is Z's legal guardian, signed a written consent to the contract.

**minor_cancel/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.

**minor_cancel/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 25 years old when signing the contract.

**minor_cancel/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z turned 18 one day before signing the contract.

**minor_cancel/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 17 years and 11 months old when signing the contract.

**minor_cancel/undetermined/S.E1T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's mother, who is Z's legal guardian, signed a written consent to the contract.

**minor_cancel/undetermined/S.E1F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian never gave any consent to the contract, written or oral.

**minor_cancel/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. Z's guardian is a lawyer.

**minor_cancel/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z's guardian is a lawyer.
  F3. Z was 16 years old when signing the contract.

**minor_cancel/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. Z was 16 years old when signing the contract.
  F3. The laptop is silver.

**minor_cancel/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Z signed a contract to buy a laptop and now wants to cancel it.
  F2. The laptop is silver.
  F3. Z was 16 years old when signing the contract.

## debt_limitation (tier 2, test)
RULE: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the date the claim was filed, unless the debtor acknowledged the debt in writing during that period.
Q: Is the debt claim time-barred?

**debt_limitation/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2020.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 28 February 2024.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 March 2024.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.

**debt_limitation/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor e-mailed the creditor the sentence 'I know I still owe you the 5,000 dollars.'

**debt_limitation/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor told the creditor by phone 'I will pay you back', but never wrote about the debt.

**debt_limitation/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. The debtor never wrote to the creditor about the debt.
  F4. The debtor has since moved to another country.

**debt_limitation/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debtor has since moved to another country.
  F3. The creditor filed the lawsuit on 5 May 2024.
  F4. The debtor never wrote to the creditor about the debt.

**debt_limitation/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. The debtor never wrote to the creditor about the debt.
  F4. The debt was for the purchase of a used car.

**debt_limitation/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debt was for the purchase of a used car.
  F3. The creditor filed the lawsuit on 5 May 2024.
  F4. The debtor never wrote to the creditor about the debt.

**debt_limitation/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.

**debt_limitation/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 March 2024.
  F3. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.

**debt_limitation/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor told the creditor by phone 'I will pay you back', but never wrote about the debt.

**debt_limitation/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor e-mailed the creditor the sentence 'I know I still owe you the 5,000 dollars.'

**debt_limitation/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.
  F4. The debtor has since moved to another country.

**debt_limitation/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debtor has since moved to another country.
  F3. The creditor filed the lawsuit on 5 May 2024.
  F4. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.

**debt_limitation/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.
  F4. The debt was for the purchase of a used car.

**debt_limitation/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debt was for the purchase of a used car.
  F3. The creditor filed the lawsuit on 5 May 2024.
  F4. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.

**debt_limitation/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debtor never wrote to the creditor about the debt.

**debt_limitation/undetermined/S.A1T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2024.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/undetermined/S.A1F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The creditor filed the lawsuit on 5 May 2020.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/undetermined/F.E1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. In 2019 the debtor sent the creditor a signed letter acknowledging the debt.

**debt_limitation/undetermined/N3.E1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. In 2019 the debtor e-mailed the creditor the sentence 'I know I still owe you the 5,000 dollars.'

**debt_limitation/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. In 2019 the debtor told the creditor by phone 'I will pay you back', but never wrote about the debt.

**debt_limitation/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debtor never wrote to the creditor about the debt.
  F3. The debtor has since moved to another country.

**debt_limitation/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debtor has since moved to another country.
  F3. The debtor never wrote to the creditor about the debt.

**debt_limitation/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debtor never wrote to the creditor about the debt.
  F3. The debt was for the purchase of a used car.

**debt_limitation/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later sued the debtor for the debt.
  F2. The debt was for the purchase of a used car.
  F3. The debtor never wrote to the creditor about the debt.

## insurance_theft (tier 3, dev)
RULE: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder reported the theft to the police more than 48 hours after discovering it and reporting within 48 hours was possible.
Q: Must the insurer pay the theft claim?

**insurance_theft/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's office, which is not the insured home.
  F3. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's holiday cottage, which is not the insured home and is insured under a different policy with another insurer.
  F3. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home while H was on holiday abroad.
  F3. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/yes/F.E1**  gold=`undetermined` (base `yes`)  kind=F pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.

**insurance_theft/yes/N3.E1**  gold=`undetermined` (base `yes`)  kind=N3 pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 49 hours after discovering it.

**insurance_theft/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police exactly 48 hours after discovering it.

**insurance_theft/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 6 hours after discovering it.
  F4. H had made two earlier theft claims under the same policy.

**insurance_theft/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. H had made two earlier theft claims under the same policy.
  F3. The theft took place at H's insured home.
  F4. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 6 hours after discovering it.
  F4. H's home has a red front door.

**insurance_theft/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. H's home has a red front door.
  F3. The theft took place at H's insured home.
  F4. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home while H was on holiday abroad.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 6 hours after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police exactly 48 hours after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 49 hours after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/no/F.E2**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. H was unconscious in hospital for the 48 hours after discovering the theft, so H could not report it in that time.

**insurance_theft/no/N3.E2**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. H was in a remote area with no phone coverage and could reach a police station only after 3 days.

**insurance_theft/no/N.E2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. H was busy with work during those 48 hours but was free to visit the police station at any time.

**insurance_theft/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.
  F5. H had made two earlier theft claims under the same policy.

**insurance_theft/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H had made two earlier theft claims under the same policy.
  F4. H reported the theft to the police 5 days after discovering it.
  F5. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.
  F5. H's home has a red front door.

**insurance_theft/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H's home has a red front door.
  F4. H reported the theft to the police 5 days after discovering it.
  F5. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.

**insurance_theft/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's office, which is not the insured home.
  F3. H reported the theft to the police 5 days after discovering it.

**insurance_theft/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's holiday cottage, which is not the insured home and is insured under a different policy with another insurer.
  F3. H reported the theft to the police 5 days after discovering it.

**insurance_theft/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home while H was on holiday abroad.
  F3. H reported the theft to the police 5 days after discovering it.

**insurance_theft/undetermined/F.E1**  gold=`yes` (base `undetermined`)  kind=F pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 6 hours after discovering it.

**insurance_theft/undetermined/N3.E1**  gold=`yes` (base `undetermined`)  kind=N3 pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police exactly 48 hours after discovering it.

**insurance_theft/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 49 hours after discovering it.

**insurance_theft/undetermined/S.E2T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. Nothing prevented H from reporting the theft within 48 hours.

**insurance_theft/undetermined/S.E2F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. H was unconscious in hospital for the 48 hours after discovering the theft, so H could not report it in that time.

**insurance_theft/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. H had made two earlier theft claims under the same policy.

**insurance_theft/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. H had made two earlier theft claims under the same policy.
  F3. The theft took place at H's insured home.
  F4. H reported the theft to the police 5 days after discovering it.

**insurance_theft/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. The theft took place at H's insured home.
  F3. H reported the theft to the police 5 days after discovering it.
  F4. H's home has a red front door.

**insurance_theft/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Policyholder H holds a home insurance policy and filed a theft claim.
  F2. H's home has a red front door.
  F3. The theft took place at H's insured home.
  F4. H reported the theft to the police 5 days after discovering it.

## contract_breach (tier 3, test)
RULE: A party is liable for breach of contract if and only if it failed to perform the contract, unless the failure was caused by an event that was both unforeseeable and beyond the party's control.
Q: Is the seller liable for breach of contract?

**contract_breach/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered all 100 units on 30 May.

**contract_breach/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered all 100 units on 1 June at 23:50, ten minutes before the deadline.

**contract_breach/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered 40 of the 100 units by 1 June and said the rest would follow later.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had no precedent anywhere in the country in the past 200 years.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had been publicly announced two months before the delivery date.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/yes/N.E2**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.
  F4. The event that stopped S from delivering was caused by a government order that S had no power to change.

**contract_breach/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.
  F4. The event that stopped S from delivering was entirely outside S's control.
  F5. S had successfully delivered goods to B on four earlier occasions.

**contract_breach/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. S had successfully delivered goods to B on four earlier occasions.
  F4. The event that stopped S from delivering is one that occurs in that region every spring.
  F5. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.
  F4. The event that stopped S from delivering was entirely outside S's control.
  F5. The units are small plastic toys.

**contract_breach/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The units are small plastic toys.
  F4. The event that stopped S from delivering is one that occurs in that region every spring.
  F5. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered 40 of the 100 units by 1 June and said the rest would follow later.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had been publicly announced two months before the delivery date.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had no precedent anywhere in the country in the past 200 years.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/F.E2**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. S could have prevented the event that stopped it from delivering simply by giving an instruction to its own staff.

**contract_breach/no/N3.E2**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was caused by a third party, but S could have prevented it at any time by paying a small fee.

**contract_breach/no/N.E2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was caused by a government order that S had no power to change.

**contract_breach/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was entirely outside S's control.
  F5. S had successfully delivered goods to B on four earlier occasions.

**contract_breach/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. S had successfully delivered goods to B on four earlier occasions.
  F4. The event that stopped S from delivering had never before occurred in that region.
  F5. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was entirely outside S's control.
  F5. The units are small plastic toys.

**contract_breach/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The units are small plastic toys.
  F4. The event that stopped S from delivering had never before occurred in that region.
  F5. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.

**contract_breach/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered all 100 units on 30 May.

**contract_breach/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered all 100 units on 1 June at 23:50, ten minutes before the deadline.

**contract_breach/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered 40 of the 100 units by 1 June and said the rest would follow later.
  F3. The event that stopped S from delivering had never before occurred in that region.

**contract_breach/undetermined/F.E1**  gold=`yes` (base `undetermined`)  kind=F pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering is one that occurs in that region every spring.

**contract_breach/undetermined/N3.E1**  gold=`yes` (base `undetermined`)  kind=N3 pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had been publicly announced two months before the delivery date.

**contract_breach/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had no precedent anywhere in the country in the past 200 years.

**contract_breach/undetermined/S.E2T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The event that stopped S from delivering was entirely outside S's control.

**contract_breach/undetermined/S.E2F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. S could have prevented the event that stopped it from delivering simply by giving an instruction to its own staff.

**contract_breach/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. S had successfully delivered goods to B on four earlier occasions.

**contract_breach/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S had successfully delivered goods to B on four earlier occasions.
  F3. S delivered none of the units by 1 June.
  F4. The event that stopped S from delivering had never before occurred in that region.

**contract_breach/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. S delivered none of the units by 1 June.
  F3. The event that stopped S from delivering had never before occurred in that region.
  F4. The units are small plastic toys.

**contract_breach/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Seller S agreed to deliver 100 units to Buyer B by 1 June.
  F2. The units are small plastic toys.
  F3. S delivered none of the units by 1 June.
  F4. The event that stopped S from delivering had never before occurred in that region.

## dismissal_no_notice (tier 3, test)
RULE: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) and the employer dismissed the worker within 7 days of learning of the misconduct, unless the worker was protected by a written job-protection agreement signed by the employer.
Q: May the employer dismiss the worker without notice?

**dismissal_no_notice/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W arrived late to work twice in one month and committed no theft, violence or fraud.
  F3. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W argued loudly with a customer and was asked to leave the workshop, but touched and threatened nobody.
  F3. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till, but only 5 dollars.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/F.A2**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 20 days after learning of the misconduct.
  F4. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/N3.A2**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M learned of the misconduct on 1 March, and although M discussed it with W on 4 March, M dismissed W only on 10 March.
  F4. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/N.A2**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M learned of the misconduct on 1 March, was away on business until 5 March, and dismissed W on 7 March.
  F4. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. M had signed a written agreement promising W protection from dismissal without notice.

**dismissal_no_notice/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. A written job-protection agreement between M and W had been signed by M and W in a ceremony attended by the whole staff, and a copy was filed with the labour office.

**dismissal_no_notice/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. M had orally promised W that W would never be dismissed without notice, but nothing was written down.

**dismissal_no_notice/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. W had no written agreement with M beyond the standard employment contract.
  F5. W had worked for M for twelve years.

**dismissal_no_notice/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. W had worked for M for twelve years.
  F4. M dismissed W 3 days after learning of the misconduct.
  F5. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. W had no written agreement with M beyond the standard employment contract.
  F5. M's workshop has 20 employees.

**dismissal_no_notice/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M's workshop has 20 employees.
  F4. M dismissed W 3 days after learning of the misconduct.
  F5. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 20 days after learning of the misconduct.

**dismissal_no_notice/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till, but only 5 dollars.
  F3. M dismissed W 20 days after learning of the misconduct.

**dismissal_no_notice/no/F.A2**  gold=`undetermined` (base `no`)  kind=F pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.

**dismissal_no_notice/no/N3.A2**  gold=`undetermined` (base `no`)  kind=N3 pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M learned of the misconduct on 1 March, was away on business until 5 March, and dismissed W on 7 March.

**dismissal_no_notice/no/N.A2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M learned of the misconduct on 1 March, and although M discussed it with W on 4 March, M dismissed W only on 10 March.

**dismissal_no_notice/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 20 days after learning of the misconduct.
  F4. W had worked for M for twelve years.

**dismissal_no_notice/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W had worked for M for twelve years.
  F3. W stole cash from the till.
  F4. M dismissed W 20 days after learning of the misconduct.

**dismissal_no_notice/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 20 days after learning of the misconduct.
  F4. M's workshop has 20 employees.

**dismissal_no_notice/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. M's workshop has 20 employees.
  F3. W stole cash from the till.
  F4. M dismissed W 20 days after learning of the misconduct.

**dismissal_no_notice/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.

**dismissal_no_notice/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W arrived late to work twice in one month and committed no theft, violence or fraud.

**dismissal_no_notice/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W argued loudly with a customer and was asked to leave the workshop, but touched and threatened nobody.

**dismissal_no_notice/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till, but only 5 dollars.
  F3. M dismissed W 3 days after learning of the misconduct.

**dismissal_no_notice/undetermined/F.A2**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 20 days after learning of the misconduct.

**dismissal_no_notice/undetermined/N3.A2**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M learned of the misconduct on 1 March, and although M discussed it with W on 4 March, M dismissed W only on 10 March.

**dismissal_no_notice/undetermined/N.A2**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M learned of the misconduct on 1 March, was away on business until 5 March, and dismissed W on 7 March.

**dismissal_no_notice/undetermined/S.E1T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. M had signed a written agreement promising W protection from dismissal without notice.

**dismissal_no_notice/undetermined/S.E1F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. W had no written agreement with M beyond the standard employment contract.

**dismissal_no_notice/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. W had worked for M for twelve years.

**dismissal_no_notice/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W had worked for M for twelve years.
  F3. W stole cash from the till.
  F4. M dismissed W 3 days after learning of the misconduct.

**dismissal_no_notice/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. W stole cash from the till.
  F3. M dismissed W 3 days after learning of the misconduct.
  F4. M's workshop has 20 employees.

**dismissal_no_notice/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Employer M runs a furniture workshop and dismissed worker W without notice.
  F2. M's workshop has 20 employees.
  F3. W stole cash from the till.
  F4. M dismissed W 3 days after learning of the misconduct.

## hotel_safe (tier 4, test)
RULE: A hotel must compensate a guest for stolen valuables if and only if the valuables had been deposited in the hotel safe at the time of the theft and the theft was reported to the hotel management within 24 hours of the guest discovering it.
Q: Must the hotel compensate the guest?

**hotel_safe/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch in the key-locked drawer of the room's wardrobe, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch, together with G's passport, in the hotel safe in a sealed envelope on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/F.A2**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 3 days after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/N3.A2**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the police 2 hours after discovering it and to the hotel manager 26 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/N.A2**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft first to the police and then to the hotel manager, 20 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.
  F10. G had stayed at the Hotel Aurora on three earlier occasions.

**hotel_safe/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. G had stayed at the Hotel Aurora on three earlier occasions.
  F6. When G returned in the evening, G found that G's watch was missing.
  F7. The hotel's restaurant had been fully booked that night.
  F8. G reported the theft to the hotel manager 2 hours after discovering it.
  F9. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F10. G now asks the hotel to compensate for the missing watch.

**hotel_safe/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.
  F10. The hotel lobby has a large green carpet.

**hotel_safe/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. The hotel lobby has a large green carpet.
  F6. When G returned in the evening, G found that G's watch was missing.
  F7. The hotel's restaurant had been fully booked that night.
  F8. G reported the theft to the hotel manager 2 hours after discovering it.
  F9. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F10. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/F.A1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/N3.A1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch, together with G's passport, in the hotel safe in a sealed envelope on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch in the key-locked drawer of the room's wardrobe, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/N.A2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft first to the police and then to the hotel manager, 20 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.
  F10. G had stayed at the Hotel Aurora on three earlier occasions.

**hotel_safe/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. G had stayed at the Hotel Aurora on three earlier occasions.
  F6. When G returned in the evening, G found that G's watch was missing.
  F7. The hotel's restaurant had been fully booked that night.
  F8. G reported the theft to the hotel manager 2 hours after discovering it.
  F9. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F10. G now asks the hotel to compensate for the missing watch.

**hotel_safe/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.
  F10. The hotel lobby has a large green carpet.

**hotel_safe/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. The hotel lobby has a large green carpet.
  F6. When G returned in the evening, G found that G's watch was missing.
  F7. The hotel's restaurant had been fully booked that night.
  F8. G reported the theft to the hotel manager 2 hours after discovering it.
  F9. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F10. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F8. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch on the bedside table in room 412, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F8. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had left the watch in the key-locked drawer of the room's wardrobe, not in the hotel safe.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F8. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch, together with G's passport, in the hotel safe in a sealed envelope on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F8. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/S.A2T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 2 hours after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/S.A2F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. G reported the theft to the hotel manager 3 days after discovering it.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F8. G now asks the hotel to compensate for the missing watch.
  F9. G had stayed at the Hotel Aurora on three earlier occasions.

**hotel_safe/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. G had stayed at the Hotel Aurora on three earlier occasions.
  F6. When G returned in the evening, G found that G's watch was missing.
  F7. The hotel's restaurant had been fully booked that night.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

**hotel_safe/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. When G returned in the evening, G found that G's watch was missing.
  F6. The hotel's restaurant had been fully booked that night.
  F7. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F8. G now asks the hotel to compensate for the missing watch.
  F9. The hotel lobby has a large green carpet.

**hotel_safe/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
  F2. The hotel has four stars and 120 rooms.
  F3. On the fifth day G travelled to a nearby town for a business meeting.
  F4. G had deposited the watch in the hotel safe at reception on the first day of the stay.
  F5. The hotel lobby has a large green carpet.
  F6. When G returned in the evening, G found that G's watch was missing.
  F7. The hotel's restaurant had been fully booked that night.
  F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
  F9. G now asks the hotel to compensate for the missing watch.

## licence_revocation (tier 4, dev)
RULE: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation, unless the violation was corrected within 30 days after the city's written notice.
Q: May the city revoke the restaurant's licence?

**licence_revocation/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 75 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. R committed no safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.

**licence_revocation/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found only a minor paint defect on R's dining-room wall, which is not a safety issue, so R committed no safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.

**licence_revocation/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 75 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 12 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation on the 30th day after receiving the city's written notice, which is within the 30-day period.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R received the city's written notice on 1 March and started repair work on 10 March, but the repair was finished only on 5 May.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 75 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.
  F9. R's owner has run two other restaurants in the city.

**licence_revocation/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. R's owner has run two other restaurants in the city.
  F6. The inspector also praised R's menu labelling.
  F7. R corrected the violation 75 days after receiving the city's written notice.
  F8. R's owner has since applied to extend the opening hours.
  F9. The city now considers revoking R's licence.

**licence_revocation/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 75 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.
  F9. R's dining room has twelve tables.

**licence_revocation/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. R's dining room has twelve tables.
  F6. The inspector also praised R's menu labelling.
  F7. R corrected the violation 75 days after receiving the city's written notice.
  F8. R's owner has since applied to extend the opening hours.
  F9. The city now considers revoking R's licence.

**licence_revocation/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 12 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 12 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 75 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R received the city's written notice on 1 March and started repair work on 10 March, but the repair was finished only on 5 May.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation on the 30th day after receiving the city's written notice, which is within the 30-day period.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 12 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.
  F9. R's owner has run two other restaurants in the city.

**licence_revocation/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. R's owner has run two other restaurants in the city.
  F6. The inspector also praised R's menu labelling.
  F7. R corrected the violation 12 days after receiving the city's written notice.
  F8. R's owner has since applied to extend the opening hours.
  F9. The city now considers revoking R's licence.

**licence_revocation/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 12 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.
  F9. R's dining room has twelve tables.

**licence_revocation/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. R's dining room has twelve tables.
  F6. The inspector also praised R's menu labelling.
  F7. R corrected the violation 12 days after receiving the city's written notice.
  F8. R's owner has since applied to extend the opening hours.
  F9. The city now considers revoking R's licence.

**licence_revocation/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.

**licence_revocation/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. R committed no safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.

**licence_revocation/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found only a minor paint defect on R's dining-room wall, which is not a safety issue, so R committed no safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.

**licence_revocation/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.

**licence_revocation/undetermined/S.E1T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 12 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/undetermined/S.E1F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R corrected the violation 75 days after receiving the city's written notice.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.
  F8. R's owner has run two other restaurants in the city.

**licence_revocation/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. R's owner has run two other restaurants in the city.
  F5. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F6. The inspector also praised R's menu labelling.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

**licence_revocation/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F5. The inspector also praised R's menu labelling.
  F6. R's owner has since applied to extend the opening hours.
  F7. The city now considers revoking R's licence.
  F8. R's dining room has twelve tables.

**licence_revocation/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Restaurant R has operated in the city centre for nine years.
  F2. R employs 14 staff and serves about 200 meals per day.
  F3. In March the city's food-safety office carried out an inspection of R.
  F4. R's dining room has twelve tables.
  F5. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
  F6. The inspector also praised R's menu labelling.
  F7. R's owner has since applied to extend the opening hours.
  F8. The city now considers revoking R's licence.

## protected_tenant (tier 3, dev)
RULE: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice, unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent.
Q: Must the tenant vacate the flat?

**protected_tenant/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is not a protected tenant.

**protected_tenant/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L never gave T any termination notice.
  F3. T is not a protected tenant.

**protected_tenant/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L told T orally, in front of two witnesses, that the tenancy was ending, but gave T nothing in writing.
  F3. T is not a protected tenant.

**protected_tenant/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L e-mailed T a termination notice, which T opened and read.
  F3. T is not a protected tenant.

**protected_tenant/yes/F.E1**  gold=`undetermined` (base `yes`)  kind=F pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.

**protected_tenant/yes/N3.E1**  gold=`undetermined` (base `yes`)  kind=N3 pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T has been a protected tenant since the start of the tenancy, five years ago.

**protected_tenant/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T applied to become a protected tenant, but the application has not been approved, so T is not a protected tenant.

**protected_tenant/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is not a protected tenant.
  F4. L raised T's rent by 5 percent last year.

**protected_tenant/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Tenant T rents a flat from landlord L.
  F2. L raised T's rent by 5 percent last year.
  F3. L gave T a written termination notice.
  F4. T is not a protected tenant.

**protected_tenant/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is not a protected tenant.
  F4. The flat has a balcony facing north.

**protected_tenant/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Tenant T rents a flat from landlord L.
  F2. The flat has a balcony facing north.
  F3. L gave T a written termination notice.
  F4. T is not a protected tenant.

**protected_tenant/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes 1 month of unpaid rent.

**protected_tenant/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L e-mailed T a termination notice, which T opened and read.
  F3. T is a protected tenant.
  F4. T owes 1 month of unpaid rent.

**protected_tenant/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is not a protected tenant.

**protected_tenant/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T applied to become a protected tenant, but the application has not been approved, so T is not a protected tenant.

**protected_tenant/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T has been a protected tenant since the start of the tenancy, five years ago.
  F4. T owes 1 month of unpaid rent.

**protected_tenant/no/F.E2**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes 3 months of unpaid rent.

**protected_tenant/no/N3.E2**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes unpaid rent for 2 months and 10 days.

**protected_tenant/no/N.E2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes unpaid rent for exactly 2 months.

**protected_tenant/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes 1 month of unpaid rent.
  F5. L raised T's rent by 5 percent last year.

**protected_tenant/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. L raised T's rent by 5 percent last year.
  F4. T is a protected tenant.
  F5. T owes 1 month of unpaid rent.

**protected_tenant/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes 1 month of unpaid rent.
  F5. The flat has a balcony facing north.

**protected_tenant/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. The flat has a balcony facing north.
  F4. T is a protected tenant.
  F5. T owes 1 month of unpaid rent.

**protected_tenant/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.

**protected_tenant/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L never gave T any termination notice.
  F3. T is a protected tenant.

**protected_tenant/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L told T orally, in front of two witnesses, that the tenancy was ending, but gave T nothing in writing.
  F3. T is a protected tenant.

**protected_tenant/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L e-mailed T a termination notice, which T opened and read.
  F3. T is a protected tenant.

**protected_tenant/undetermined/F.E1**  gold=`yes` (base `undetermined`)  kind=F pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is not a protected tenant.

**protected_tenant/undetermined/N3.E1**  gold=`yes` (base `undetermined`)  kind=N3 pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T applied to become a protected tenant, but the application has not been approved, so T is not a protected tenant.

**protected_tenant/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T has been a protected tenant since the start of the tenancy, five years ago.

**protected_tenant/undetermined/S.E2T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes 3 months of unpaid rent.

**protected_tenant/undetermined/S.E2F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. T owes 1 month of unpaid rent.

**protected_tenant/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. L raised T's rent by 5 percent last year.

**protected_tenant/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Tenant T rents a flat from landlord L.
  F2. L raised T's rent by 5 percent last year.
  F3. L gave T a written termination notice.
  F4. T is a protected tenant.

**protected_tenant/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Tenant T rents a flat from landlord L.
  F2. L gave T a written termination notice.
  F3. T is a protected tenant.
  F4. The flat has a balcony facing north.

**protected_tenant/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Tenant T rents a flat from landlord L.
  F2. The flat has a balcony facing north.
  F3. L gave T a written termination notice.
  F4. T is a protected tenant.

## severance_pay (tier 3, dev)
RULE: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years, unless the employee was dismissed for gross misconduct or the employee signed a written waiver of severance pay.
Q: Is the employee entitled to severance pay?

**severance_pay/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.

**severance_pay/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. E resigned of E's own accord.
  F3. E had worked for the employer for 5 years.

**severance_pay/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E could stay, but E decided to resign after a disagreement with a colleague.
  F3. E had worked for the employer for 5 years.

**severance_pay/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign and was dismissed the next day.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.

**severance_pay/yes/F.A2**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 8 months.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.

**severance_pay/yes/N3.A2**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 1 year and 11 months.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.

**severance_pay/yes/N.A2**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for exactly 2 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.

**severance_pay/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.
  F5. E signed nothing about severance pay.

**severance_pay/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely repeatedly threatening colleagues with violence, after a disciplinary hearing at which E was represented.
  F5. E signed nothing about severance pay.

**severance_pay/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for being late to work on 6 occasions, which the employer's handbook classes as minor misconduct.
  F5. E signed nothing about severance pay.

**severance_pay/yes/F.E2**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed a written waiver of severance pay.

**severance_pay/yes/N3.E2**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed a written waiver of all claims against the employer, which listed severance pay among them.

**severance_pay/yes/N.E2**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E said to the manager 'I do not need any severance pay', but signed nothing.

**severance_pay/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.
  F6. E had received a bonus the previous year.

**severance_pay/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had received a bonus the previous year.
  F4. E had worked for the employer for 5 years.
  F5. E was not dismissed for gross misconduct; the employer closed E's department.
  F6. E signed nothing about severance pay.

**severance_pay/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.
  F6. The logistics company has a warehouse near the airport.

**severance_pay/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. The logistics company has a warehouse near the airport.
  F4. E had worked for the employer for 5 years.
  F5. E was not dismissed for gross misconduct; the employer closed E's department.
  F6. E signed nothing about severance pay.

**severance_pay/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.

**severance_pay/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign and was dismissed the next day.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.

**severance_pay/no/N.A2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for exactly 2 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.

**severance_pay/no/F.E1**  gold=`undetermined` (base `no`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/no/N3.E1**  gold=`undetermined` (base `no`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for being late to work on 6 occasions, which the employer's handbook classes as minor misconduct.

**severance_pay/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely repeatedly threatening colleagues with violence, after a disciplinary hearing at which E was represented.

**severance_pay/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.
  F5. E had received a bonus the previous year.

**severance_pay/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had received a bonus the previous year.
  F4. E had worked for the employer for 5 years.
  F5. E was dismissed for gross misconduct, namely stealing company equipment.

**severance_pay/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.
  F5. The logistics company has a warehouse near the airport.

**severance_pay/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. The logistics company has a warehouse near the airport.
  F4. E had worked for the employer for 5 years.
  F5. E was dismissed for gross misconduct, namely stealing company equipment.

**severance_pay/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. E resigned of E's own accord.
  F3. E had worked for the employer for 5 years.

**severance_pay/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E could stay, but E decided to resign after a disagreement with a colleague.
  F3. E had worked for the employer for 5 years.

**severance_pay/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign and was dismissed the next day.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/undetermined/F.A2**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 8 months.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/undetermined/N3.A2**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 1 year and 11 months.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/undetermined/N.A2**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for exactly 2 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/undetermined/F.E1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely stealing company equipment.

**severance_pay/undetermined/N3.E1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for gross misconduct, namely repeatedly threatening colleagues with violence, after a disciplinary hearing at which E was represented.

**severance_pay/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was dismissed for being late to work on 6 occasions, which the employer's handbook classes as minor misconduct.

**severance_pay/undetermined/S.E2T**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed a written waiver of severance pay.

**severance_pay/undetermined/S.E2F**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E signed nothing about severance pay.

**severance_pay/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. E had received a bonus the previous year.

**severance_pay/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had received a bonus the previous year.
  F4. E had worked for the employer for 5 years.
  F5. E was not dismissed for gross misconduct; the employer closed E's department.

**severance_pay/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. E had worked for the employer for 5 years.
  F4. E was not dismissed for gross misconduct; the employer closed E's department.
  F5. The logistics company has a warehouse near the airport.

**severance_pay/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Employee E worked for a logistics company.
  F2. The employer told E that E's position was being eliminated and terminated E's employment.
  F3. The logistics company has a warehouse near the airport.
  F4. E had worked for the employer for 5 years.
  F5. E was not dismissed for gross misconduct; the employer closed E's department.

## defective_goods (tier 4, dev)
RULE: A buyer may return a product for a refund if and only if the product was defective on delivery and the buyer notified the seller of the defect within 14 days of delivery, unless the seller had told the buyer of the defect before the sale.
Q: May B return the machine for a refund?

**defective_goods/yes/base**  gold=`yes` (base `yes`)  kind=base pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/F.A1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. The machine was delivered to B's home on 12 May.
  F5. The machine was not defective on delivery: it worked perfectly when B first ran it.
  F6. B's neighbour, who is an electrician, offered to help B with the installation.
  F7. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/N3.A1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. The machine was delivered to B's home on 12 May.
  F5. The machine's motor broke down 3 months after delivery because B overloaded it, and the repair report found no fault from manufacture, so the machine was not defective on delivery.
  F6. B's neighbour, who is an electrician, offered to help B with the installation.
  F7. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/N.A1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine worked on the first cycle, but the motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the machine was defective on delivery.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/F.A2**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 30 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/N3.A2**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 27 May, 15 days after delivery.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/N.A2**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault by e-mail on 26 May, 14 days after delivery.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/F.E1**  gold=`no` (base `yes`)  kind=F pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/N3.E1**  gold=`no` (base `yes`)  kind=N3 pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B by telephone that its motor was faulty, and B repeated the warning back to S.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/N.E1**  gold=`yes` (base `yes`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S's website listed the machine as 'factory second', but said nothing about any fault in it.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/I1.end**  gold=`yes` (base `yes`)  kind=I1 pos=end
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.
  F10. B had bought three other appliances from S without any problem.

**defective_goods/yes/I1.middle**  gold=`yes` (base `yes`)  kind=I1 pos=middle
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. B had bought three other appliances from S without any problem.
  F6. The machine was delivered to B's home on 12 May.
  F7. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F8. B's neighbour, who is an electrician, offered to help B with the installation.
  F9. B told S about the fault on 20 May.
  F10. B has since asked S for a refund of the 480 dollars.

**defective_goods/yes/I2.end**  gold=`yes` (base `yes`)  kind=I2 pos=end
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.
  F10. The machine is white and has a 7 kg drum.

**defective_goods/yes/I2.middle**  gold=`yes` (base `yes`)  kind=I2 pos=middle
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine is white and has a 7 kg drum.
  F6. The machine was delivered to B's home on 12 May.
  F7. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F8. B's neighbour, who is an electrician, offered to help B with the installation.
  F9. B told S about the fault on 20 May.
  F10. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/base**  gold=`no` (base `no`)  kind=base pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/N.A1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine worked on the first cycle, but the motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the machine was defective on delivery.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/N.A2**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault by e-mail on 26 May, 14 days after delivery.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/F.E1**  gold=`yes` (base `no`)  kind=F pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/N3.E1**  gold=`yes` (base `no`)  kind=N3 pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S's website listed the machine as 'factory second', but said nothing about any fault in it.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/N.E1**  gold=`no` (base `no`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B by telephone that its motor was faulty, and B repeated the warning back to S.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/I1.end**  gold=`no` (base `no`)  kind=I1 pos=end
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.
  F10. B had bought three other appliances from S without any problem.

**defective_goods/no/I1.middle**  gold=`no` (base `no`)  kind=I1 pos=middle
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. B had bought three other appliances from S without any problem.
  F6. The machine was delivered to B's home on 12 May.
  F7. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F8. B's neighbour, who is an electrician, offered to help B with the installation.
  F9. B told S about the fault on 20 May.
  F10. B has since asked S for a refund of the 480 dollars.

**defective_goods/no/I2.end**  gold=`no` (base `no`)  kind=I2 pos=end
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.
  F10. The machine is white and has a 7 kg drum.

**defective_goods/no/I2.middle**  gold=`no` (base `no`)  kind=I2 pos=middle
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine is white and has a 7 kg drum.
  F6. The machine was delivered to B's home on 12 May.
  F7. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F8. B's neighbour, who is an electrician, offered to help B with the installation.
  F9. B told S about the fault on 20 May.
  F10. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/base**  gold=`undetermined` (base `undetermined`)  kind=base pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/F.A1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. The machine was delivered to B's home on 12 May.
  F5. The machine was not defective on delivery: it worked perfectly when B first ran it.
  F6. B's neighbour, who is an electrician, offered to help B with the installation.
  F7. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/N3.A1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. The machine was delivered to B's home on 12 May.
  F5. The machine's motor broke down 3 months after delivery because B overloaded it, and the repair report found no fault from manufacture, so the machine was not defective on delivery.
  F6. B's neighbour, who is an electrician, offered to help B with the installation.
  F7. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/N.A1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine worked on the first cycle, but the motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the machine was defective on delivery.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/S.A2T**  gold=`yes` (base `undetermined`)  kind=S pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 20 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/S.A2F**  gold=`no` (base `undetermined`)  kind=S pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B told S about the fault on 30 May.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/F.E1**  gold=`no` (base `undetermined`)  kind=F pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B in writing that its motor was faulty.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/N3.E1**  gold=`no` (base `undetermined`)  kind=N3 pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. Before B bought the machine, S warned B by telephone that its motor was faulty, and B repeated the warning back to S.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/N.E1**  gold=`undetermined` (base `undetermined`)  kind=N pos=slot
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S's website listed the machine as 'factory second', but said nothing about any fault in it.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/I1.end**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=end
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.
  F9. B had bought three other appliances from S without any problem.

**defective_goods/undetermined/I1.middle**  gold=`undetermined` (base `undetermined`)  kind=I1 pos=middle
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. B had bought three other appliances from S without any problem.
  F6. The machine was delivered to B's home on 12 May.
  F7. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F8. B's neighbour, who is an electrician, offered to help B with the installation.
  F9. B has since asked S for a refund of the 480 dollars.

**defective_goods/undetermined/I2.end**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=end
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine was delivered to B's home on 12 May.
  F6. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F7. B's neighbour, who is an electrician, offered to help B with the installation.
  F8. B has since asked S for a refund of the 480 dollars.
  F9. The machine is white and has a 7 kg drum.

**defective_goods/undetermined/I2.middle**  gold=`undetermined` (base `undetermined`)  kind=I2 pos=middle
  F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
  F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
  F3. S's standard warranty on all machines is 24 months.
  F4. S told B nothing about any fault before B bought the machine.
  F5. The machine is white and has a 7 kg drum.
  F6. The machine was delivered to B's home on 12 May.
  F7. The machine was defective on delivery: when B first ran it, the drum would not spin because of a faulty motor.
  F8. B's neighbour, who is an electrician, offered to help B with the installation.
  F9. B has since asked S for a refund of the 480 dollars.
