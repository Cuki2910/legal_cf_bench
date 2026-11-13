# V2 review — human item review PENDING; no model run

## refund_window / dev / c1039fd6dd60
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 2 days after buying it.
Computed gold: `yes`

## refund_window / dev / 1fc73d3025e8
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 10 days after buying it.
Computed gold: `no`

## refund_window / dev / 77efc77b7384
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 1 day after buying it, after wearing it once.
Computed gold: `yes`

## refund_window / dev / b9cb99a33f91
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 2 days after buying it.
I. The jacket was sold at a discount of 30 percent.
Computed gold: `yes`

## refund_window / dev / f7c1e62a64d2
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
I. The jacket was sold at a discount of 30 percent.
F2. C physically brought the jacket back to the shop 2 days after buying it.
Computed gold: `yes`

## refund_window / dev / afdfa313fcba
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 2 days after buying it.
I. The shop is located on the second floor of a mall.
Computed gold: `yes`

## refund_window / dev / 45fc35f53fd2
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
I. The shop is located on the second floor of a mall.
F2. C physically brought the jacket back to the shop 2 days after buying it.
Computed gold: `yes`

## refund_window / dev / 084e2791a0bb
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C first contacted the shop about a return 2 days after buying the jacket, but physically brought the jacket back to the shop 6 days after buying it.
Computed gold: `no`

## refund_window / dev / fb26b0eda02b
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 10 days after buying it.
I. The jacket was sold at a discount of 30 percent.
Computed gold: `no`

## refund_window / dev / faeeb999d1d8
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
I. The jacket was sold at a discount of 30 percent.
F2. C physically brought the jacket back to the shop 10 days after buying it.
Computed gold: `no`

## refund_window / dev / f5cc3ef840f5
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
F2. C physically brought the jacket back to the shop 10 days after buying it.
I. The shop is located on the second floor of a mall.
Computed gold: `no`

## refund_window / dev / 38edfc95ea36
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
I. The shop is located on the second floor of a mall.
F2. C physically brought the jacket back to the shop 10 days after buying it.
Computed gold: `no`

## refund_window / dev / b29df70b3574
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
Computed gold: `undetermined`

## refund_window / dev / c470f2782803
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
I. The jacket was sold at a discount of 30 percent.
Computed gold: `undetermined`

## refund_window / dev / 7b8d992c9b84
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
I. The jacket was sold at a discount of 30 percent.
F1. Customer C bought a jacket from a shop.
Computed gold: `undetermined`

## refund_window / dev / 05d77768a28b
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
F1. Customer C bought a jacket from a shop.
I. The shop is located on the second floor of a mall.
Computed gold: `undetermined`

## refund_window / dev / 519544f9b595
Rule: A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.
Question: Must the shop refund the item?
I. The shop is located on the second floor of a mall.
F1. Customer C bought a jacket from a shop.
Computed gold: `undetermined`

## noise_fine / dev / cda973b29bc4
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 23:30.
Computed gold: `yes`

## noise_fine / dev / 89e1728d4112
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 15:00.
Computed gold: `no`

## noise_fine / dev / 3ae06933c58d
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 05:45, shortly before sunrise.
Computed gold: `yes`

## noise_fine / dev / 17d83ce633d4
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 23:30.
I. R had received a written warning about noise one year earlier.
Computed gold: `yes`

## noise_fine / dev / 937e409b5006
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
I. R had received a written warning about noise one year earlier.
F2. R played the loud music at 23:30.
Computed gold: `yes`

## noise_fine / dev / fcf11e616236
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 23:30.
I. R's flat is on the fourth floor.
Computed gold: `yes`

## noise_fine / dev / 5c0fd3dad865
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
I. R's flat is on the fourth floor.
F2. R played the loud music at 23:30.
Computed gold: `yes`

## noise_fine / dev / 9058ac1a8abf
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 21:50.
Computed gold: `no`

## noise_fine / dev / 7c577a7e7b5d
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 15:00.
I. R had received a written warning about noise one year earlier.
Computed gold: `no`

## noise_fine / dev / 6a4a6a246c10
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
I. R had received a written warning about noise one year earlier.
F2. R played the loud music at 15:00.
Computed gold: `no`

## noise_fine / dev / 8cd36c3d3001
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
F2. R played the loud music at 15:00.
I. R's flat is on the fourth floor.
Computed gold: `no`

## noise_fine / dev / bfa72d0250ff
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
I. R's flat is on the fourth floor.
F2. R played the loud music at 15:00.
Computed gold: `no`

## noise_fine / dev / 1a67331ebf72
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
Computed gold: `undetermined`

## noise_fine / dev / 7c6e41515e74
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
I. R had received a written warning about noise one year earlier.
Computed gold: `undetermined`

## noise_fine / dev / d6ed974b1564
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
I. R had received a written warning about noise one year earlier.
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
Computed gold: `undetermined`

## noise_fine / dev / 6039f6a51f09
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
I. R's flat is on the fourth floor.
Computed gold: `undetermined`

## noise_fine / dev / a23e5f9ccaa3
Rule: A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).
Question: Must the resident pay a noise fine?
I. R's flat is on the fourth floor.
F1. Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.
Computed gold: `undetermined`

## witnessed_contract / dev / e83e5fb56ef2
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. Two adults, neither of whom is P or Q, watched both P and Q sign the contract.
Computed gold: `yes`

## witnessed_contract / dev / 026832b9937f
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. No adult other than P and Q watched either party sign the contract.
Computed gold: `no`

## witnessed_contract / dev / ae47279302bf
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. Two adults, neither of whom is P or Q, watched both P and Q sign the contract; one of these adults is P's cousin.
Computed gold: `yes`

## witnessed_contract / dev / daf93da4a9d2
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. Two adults, neither of whom is P or Q, watched both P and Q sign the contract.
I. The contract price was 200 dollars.
Computed gold: `yes`

## witnessed_contract / dev / 02ac563e8c73
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
I. The contract price was 200 dollars.
F2. Two adults, neither of whom is P or Q, watched both P and Q sign the contract.
Computed gold: `yes`

## witnessed_contract / dev / efd48f93b2e9
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. Two adults, neither of whom is P or Q, watched both P and Q sign the contract.
I. The contract was written in blue ink.
Computed gold: `yes`

## witnessed_contract / dev / 327de3d64ad7
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
I. The contract was written in blue ink.
F2. Two adults, neither of whom is P or Q, watched both P and Q sign the contract.
Computed gold: `yes`

## witnessed_contract / dev / eceb67552820
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. Exactly one adult other than P and Q watched both parties sign. A second adult heard them from another room but did not see either party sign.
Computed gold: `no`

## witnessed_contract / dev / 274ffd064234
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. No adult other than P and Q watched either party sign the contract.
I. The contract price was 200 dollars.
Computed gold: `no`

## witnessed_contract / dev / f1b9249a1223
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
I. The contract price was 200 dollars.
F2. No adult other than P and Q watched either party sign the contract.
Computed gold: `no`

## witnessed_contract / dev / bd0cd5298cf5
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
F2. No adult other than P and Q watched either party sign the contract.
I. The contract was written in blue ink.
Computed gold: `no`

## witnessed_contract / dev / 47a9eb9dc18f
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
I. The contract was written in blue ink.
F2. No adult other than P and Q watched either party sign the contract.
Computed gold: `no`

## witnessed_contract / dev / 6a4cb344c8b7
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
Computed gold: `undetermined`

## witnessed_contract / dev / 04d53bea7879
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
I. The contract price was 200 dollars.
Computed gold: `undetermined`

## witnessed_contract / dev / 7d2c9c780c30
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
I. The contract price was 200 dollars.
F1. Parties P and Q signed a contract to sell a bicycle.
Computed gold: `undetermined`

## witnessed_contract / dev / 2f800a519b26
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
F1. Parties P and Q signed a contract to sell a bicycle.
I. The contract was written in blue ink.
Computed gold: `undetermined`

## witnessed_contract / dev / 223fca1e6164
Rule: A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.
Question: Is the contract valid?
I. The contract was written in blue ink.
F1. Parties P and Q signed a contract to sell a bicycle.
Computed gold: `undetermined`

## tenancy_late / dev / fc6cb8785928
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
Computed gold: `yes`

## tenancy_late / dev / c1738eb0809d
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 12 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
Computed gold: `no`

## tenancy_late / dev / 5e2278d630da
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 31 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
Computed gold: `yes`

## tenancy_late / dev / 4e5faeab0f05
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L signed a written notice accepting T's payment of the March rent.
Computed gold: `no`

## tenancy_late / dev / ae0c638f7c4c
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L told T by phone that the timing of T's March rent payment was acceptable, but never put it in writing.
Computed gold: `yes`

## tenancy_late / dev / ca8599b68ebf
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
I. T had paid every earlier month's rent on time for five years.
Computed gold: `yes`

## tenancy_late / dev / 166bfb7de61b
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
I. T had paid every earlier month's rent on time for five years.
F2. T paid the March rent 45 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
Computed gold: `yes`

## tenancy_late / dev / a2fe3eb33396
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
I. T's flat is on the fifth floor.
Computed gold: `yes`

## tenancy_late / dev / 14ceb108a481
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
I. T's flat is on the fifth floor.
F2. T paid the March rent 45 days after its due date.
F3. L never signed any written notice about T's payment of the March rent.
Computed gold: `yes`

## tenancy_late / dev / f988b1854c8e
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 31 days after its due date.
F3. L signed a written notice accepting T's payment of the March rent.
Computed gold: `no`

## tenancy_late / dev / 4972e15005a1
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L signed a written notice that began by complaining about the delay of T's March rent payment but ended with the words 'I accept this payment of the March rent.'
Computed gold: `no`

## tenancy_late / dev / c85b51fb21e4
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L signed a written notice accepting T's payment of the March rent.
I. T had paid every earlier month's rent on time for five years.
Computed gold: `no`

## tenancy_late / dev / b5d8d7bd21f3
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
I. T had paid every earlier month's rent on time for five years.
F2. T paid the March rent 45 days after its due date.
F3. L signed a written notice accepting T's payment of the March rent.
Computed gold: `no`

## tenancy_late / dev / c83f70e75c76
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
F3. L signed a written notice accepting T's payment of the March rent.
I. T's flat is on the fifth floor.
Computed gold: `no`

## tenancy_late / dev / f4fd01041bd5
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
I. T's flat is on the fifth floor.
F2. T paid the March rent 45 days after its due date.
F3. L signed a written notice accepting T's payment of the March rent.
Computed gold: `no`

## tenancy_late / dev / 4e946907240b
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
Computed gold: `undetermined`

## tenancy_late / dev / eca705e80806
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 12 days after its due date.
Computed gold: `no`

## tenancy_late / dev / 0943bdd9bd95
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 31 days after its due date.
Computed gold: `undetermined`

## tenancy_late / dev / 5892dceada4b
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
I. T had paid every earlier month's rent on time for five years.
Computed gold: `undetermined`

## tenancy_late / dev / deb56034da17
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
I. T had paid every earlier month's rent on time for five years.
F2. T paid the March rent 45 days after its due date.
Computed gold: `undetermined`

## tenancy_late / dev / b56331665b4e
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
F2. T paid the March rent 45 days after its due date.
I. T's flat is on the fifth floor.
Computed gold: `undetermined`

## tenancy_late / dev / 032a45aec159
Rule: A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).
Question: May the landlord evict the tenant?
F1. Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.
I. T's flat is on the fifth floor.
F2. T paid the March rent 45 days after its due date.
Computed gold: `undetermined`

## booking_cancel / dev / e7d7edeeb30c
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `yes`

## booking_cancel / dev / c8fb23ced37b
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 17 June.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `no`

## booking_cancel / dev / 153d5219486b
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 13 June, exactly 7 days before check-in.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `yes`

## booking_cancel / dev / 10f9c6a55f04
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
Computed gold: `no`

## booking_cancel / dev / 6e04f505569e
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The hotel's website marked the room rate as non-refundable, but V's booking, made through a travel agent, was marked refundable at the time of booking.
Computed gold: `yes`

## booking_cancel / dev / 72435d97c578
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The booking was marked fully refundable at the time of booking.
I. V had stayed at the same hotel twice before.
Computed gold: `yes`

## booking_cancel / dev / f8150974a649
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
I. V had stayed at the same hotel twice before.
F2. V cancelled the booking on 8 June.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `yes`

## booking_cancel / dev / b51ec9780d0b
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The booking was marked fully refundable at the time of booking.
I. The hotel room had a view of the sea.
Computed gold: `yes`

## booking_cancel / dev / 11cab3c168f9
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
I. The hotel room had a view of the sea.
F2. V cancelled the booking on 8 June.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `yes`

## booking_cancel / dev / 6e84ddbe43e9
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 13 June, exactly 7 days before check-in.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
Computed gold: `no`

## booking_cancel / dev / 148526165950
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. At the time of booking, the small print under the price on the booking page marked this booking 'non-refundable', and V ticked the box accepting those terms.
Computed gold: `no`

## booking_cancel / dev / 4d205f07b6c5
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
I. V had stayed at the same hotel twice before.
Computed gold: `no`

## booking_cancel / dev / 0ebfbf3b6ced
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
I. V had stayed at the same hotel twice before.
F2. V cancelled the booking on 8 June.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
Computed gold: `no`

## booking_cancel / dev / 38062bce69d6
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F2. V cancelled the booking on 8 June.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
I. The hotel room had a view of the sea.
Computed gold: `no`

## booking_cancel / dev / 78e5292629f3
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
I. The hotel room had a view of the sea.
F2. V cancelled the booking on 8 June.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
Computed gold: `no`

## booking_cancel / dev / bf3910125cbb
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `undetermined`

## booking_cancel / dev / 088e95c6a19b
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F3. The booking confirmation stated 'non-refundable' at the time of booking.
Computed gold: `no`

## booking_cancel / dev / b44a0e8e3be7
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F3. The hotel's website marked the room rate as non-refundable, but V's booking, made through a travel agent, was marked refundable at the time of booking.
Computed gold: `undetermined`

## booking_cancel / dev / 4d5fc3db206a
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F3. The booking was marked fully refundable at the time of booking.
I. V had stayed at the same hotel twice before.
Computed gold: `undetermined`

## booking_cancel / dev / 7a60fbab27ed
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
I. V had stayed at the same hotel twice before.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `undetermined`

## booking_cancel / dev / 1e621b42bcf9
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
F3. The booking was marked fully refundable at the time of booking.
I. The hotel room had a view of the sea.
Computed gold: `undetermined`

## booking_cancel / dev / d8aa6a8126fb
Rule: A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.
Question: Is the traveller entitled to a full refund for the cancelled booking?
F1. Traveller V booked a hotel room for a stay beginning on 20 June.
I. The hotel room had a view of the sea.
F3. The booking was marked fully refundable at the time of booking.
Computed gold: `undetermined`

## minor_cancel / dev / 45c74934dbd6
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
Computed gold: `yes`

## minor_cancel / dev / 5bded509d1fe
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 25 years old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
Computed gold: `no`

## minor_cancel / dev / 823af6de6b24
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 17 years and 11 months old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
Computed gold: `yes`

## minor_cancel / dev / b7761e847c67
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. Z's mother signed a written consent to the contract.
Computed gold: `no`

## minor_cancel / dev / b3e6eb6ee53c
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. Z's mother told Z orally 'go ahead and buy the laptop', and no parent of Z gave any written consent.
Computed gold: `yes`

## minor_cancel / dev / 1cdb2e066eda
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
I. Z's uncle is a lawyer.
Computed gold: `yes`

## minor_cancel / dev / 9961ec279c4d
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
I. Z's uncle is a lawyer.
F2. Z was 16 years old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
Computed gold: `yes`

## minor_cancel / dev / fbf19871360c
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
I. The laptop is silver.
Computed gold: `yes`

## minor_cancel / dev / a13aaf801576
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
I. The laptop is silver.
F2. Z was 16 years old when signing the contract.
F3. No parent of Z gave any consent to the contract, written or oral.
Computed gold: `yes`

## minor_cancel / dev / 0a03c15a3732
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 17 years and 11 months old when signing the contract.
F3. Z's mother signed a written consent to the contract.
Computed gold: `no`

## minor_cancel / dev / c63dfab8f2e6
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. Z's father wrote a short e-mail to the shop saying 'Z may buy the laptop'.
Computed gold: `no`

## minor_cancel / dev / 80c6026c535c
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. Z's mother signed a written consent to the contract.
I. Z's uncle is a lawyer.
Computed gold: `no`

## minor_cancel / dev / 1ab7d407acfb
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
I. Z's uncle is a lawyer.
F2. Z was 16 years old when signing the contract.
F3. Z's mother signed a written consent to the contract.
Computed gold: `no`

## minor_cancel / dev / 1bc0665b07ac
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
F3. Z's mother signed a written consent to the contract.
I. The laptop is silver.
Computed gold: `no`

## minor_cancel / dev / 020e303ed0cf
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
I. The laptop is silver.
F2. Z was 16 years old when signing the contract.
F3. Z's mother signed a written consent to the contract.
Computed gold: `no`

## minor_cancel / dev / 5d0048cda226
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
Computed gold: `undetermined`

## minor_cancel / dev / 00dae604903b
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 25 years old when signing the contract.
Computed gold: `no`

## minor_cancel / dev / d8de871ceacb
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 17 years and 11 months old when signing the contract.
Computed gold: `undetermined`

## minor_cancel / dev / a3157a35a624
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
I. Z's uncle is a lawyer.
Computed gold: `undetermined`

## minor_cancel / dev / b62dbf3263da
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
I. Z's uncle is a lawyer.
F2. Z was 16 years old when signing the contract.
Computed gold: `undetermined`

## minor_cancel / dev / a0b859c5b204
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
F2. Z was 16 years old when signing the contract.
I. The laptop is silver.
Computed gold: `undetermined`

## minor_cancel / dev / f7956a42572e
Rule: A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).
Question: May Z cancel the contract?
F1. Z signed a contract to buy a laptop and now wants to cancel it.
I. The laptop is silver.
F2. Z was 16 years old when signing the contract.
Computed gold: `undetermined`

## debt_limitation / dev / 7374d2181482
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `yes`

## debt_limitation / dev / e0ea4fa96c06
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2020.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `no`

## debt_limitation / dev / b8bf0c3c568a
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 March 2024.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `yes`

## debt_limitation / dev / 94c5ce9129f9
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
Computed gold: `no`

## debt_limitation / dev / 81f59884fbe5
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. Between the due date and the filing date, the debtor acknowledged the debt only orally in a phone call and made no written acknowledgment to anyone.
Computed gold: `yes`

## debt_limitation / dev / 6051ca08b148
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
I. The debtor has since moved to another country.
Computed gold: `yes`

## debt_limitation / dev / e86128d3d6e6
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
I. The debtor has since moved to another country.
F2. The creditor filed the claim on 5 May 2024.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `yes`

## debt_limitation / dev / 974e6c5b1980
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
I. The debt was for the purchase of a used car.
Computed gold: `yes`

## debt_limitation / dev / f94ee49cf3ea
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
I. The debt was for the purchase of a used car.
F2. The creditor filed the claim on 5 May 2024.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `yes`

## debt_limitation / dev / a6ec62591d8f
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 March 2024.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
Computed gold: `no`

## debt_limitation / dev / 82471d62832c
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. On 12 June 2019 the debtor e-mailed the creditor the sentence 'I know I still owe you the 5,000 dollars.'
Computed gold: `no`

## debt_limitation / dev / 60ee46867cef
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
I. The debtor has since moved to another country.
Computed gold: `no`

## debt_limitation / dev / 3be9d6144f38
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
I. The debtor has since moved to another country.
F2. The creditor filed the claim on 5 May 2024.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
Computed gold: `no`

## debt_limitation / dev / d9c6b163192d
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F2. The creditor filed the claim on 5 May 2024.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
I. The debt was for the purchase of a used car.
Computed gold: `no`

## debt_limitation / dev / cb6a217bb47e
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
I. The debt was for the purchase of a used car.
F2. The creditor filed the claim on 5 May 2024.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
Computed gold: `no`

## debt_limitation / dev / 706d2739f610
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `undetermined`

## debt_limitation / dev / 4fcd4a2d37bd
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F3. On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.
Computed gold: `no`

## debt_limitation / dev / bd450d83ad69
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F3. Between the due date and the filing date, the debtor acknowledged the debt only orally in a phone call and made no written acknowledgment to anyone.
Computed gold: `undetermined`

## debt_limitation / dev / 64584ead9b8e
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
I. The debtor has since moved to another country.
Computed gold: `undetermined`

## debt_limitation / dev / 10fdf0d6d61b
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
I. The debtor has since moved to another country.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `undetermined`

## debt_limitation / dev / a549810e9984
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
I. The debt was for the purchase of a used car.
Computed gold: `undetermined`

## debt_limitation / dev / 712720a74bc1
Rule: A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).
Question: Is the debt claim time-barred?
F1. A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.
I. The debt was for the purchase of a used car.
F3. Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.
Computed gold: `undetermined`

## insurance_theft / dev / 34db72cb39ec
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 6 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / b38a6f231593
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's office, which is not the insured home.
F3. H reported the theft to the police 6 hours after discovering it.
Computed gold: `no`

## insurance_theft / dev / 4baead6a31b0
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home while H was on holiday abroad.
F3. H reported the theft to the police 6 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / ff2841af275a
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
Computed gold: `undetermined`

## insurance_theft / dev / 7cf595807d36
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police exactly 48 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / 49e415b54f8b
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 6 hours after discovering it.
I. H had made two earlier theft claims under the same policy.
Computed gold: `yes`

## insurance_theft / dev / 0eb0accc8830
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
I. H had made two earlier theft claims under the same policy.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 6 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / 906191729ce0
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 6 hours after discovering it.
I. H's home has a red front door.
Computed gold: `yes`

## insurance_theft / dev / c45a88ac4f1c
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
I. H's home has a red front door.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 6 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / bb044097f011
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `no`

## insurance_theft / dev / f37c52e27231
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home while H was on holiday abroad.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `no`

## insurance_theft / dev / 195dce0ac051
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 6 hours after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / d9ced32b20ec
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 49 hours after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `no`

## insurance_theft / dev / c010e3be19da
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was impossible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `yes`

## insurance_theft / dev / 668ecdcd058e
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
F4. H was busy with work, but reporting the theft to the police within those 48 hours remained possible.
Computed gold: `no`

## insurance_theft / dev / d7b9d93f2ca4
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
I. H had made two earlier theft claims under the same policy.
Computed gold: `no`

## insurance_theft / dev / 9d1a31ee434d
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
I. H had made two earlier theft claims under the same policy.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `no`

## insurance_theft / dev / 13bdfe0f2172
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
I. H's home has a red front door.
Computed gold: `no`

## insurance_theft / dev / b9c2ad81f9b4
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
I. H's home has a red front door.
F3. H reported the theft to the police 5 days after discovering it.
F4. It was possible for H to report the theft to the police within the 48 hours after discovering it.
Computed gold: `no`

## insurance_theft / dev / 4b29ec89dece
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's office, which is not the insured home.
F3. H reported the theft to the police 5 days after discovering it.
Computed gold: `no`

## insurance_theft / dev / 2c04fce3796d
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home while H was on holiday abroad.
F3. H reported the theft to the police 5 days after discovering it.
Computed gold: `undetermined`

## insurance_theft / dev / a7fa7f27ddbd
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 49 hours after discovering it.
Computed gold: `undetermined`

## insurance_theft / dev / d89b9d04312a
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
I. H had made two earlier theft claims under the same policy.
Computed gold: `undetermined`

## insurance_theft / dev / 8cce88945511
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
I. H had made two earlier theft claims under the same policy.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
Computed gold: `undetermined`

## insurance_theft / dev / 0d3c0c5e48fd
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
I. H's home has a red front door.
Computed gold: `undetermined`

## insurance_theft / dev / 4d8f81890538
Rule: An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.
Question: Must the insurer pay the theft claim?
F1. Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.
I. H's home has a red front door.
F2. The theft took place at H's insured home.
F3. H reported the theft to the police 5 days after discovering it.
Computed gold: `undetermined`

## contract_breach / dev / 7977142db475
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `yes`

## contract_breach / dev / 45d08f47eab5
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered all 100 units on 30 May.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `no`

## contract_breach / dev / 3bbacb16a631
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered 40 of the 100 units by the end of 1 June and said the rest would follow later.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `yes`

## contract_breach / dev / 941fbfe2543d
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `no`

## contract_breach / dev / 0f492965368a
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. Shutdowns of this depot were rare, but a specific warning that S received before the contract was signed made the shutdown reasonably foreseeable.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `yes`

## contract_breach / dev / 26e8c47f67c3
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a flood in the region, and S could neither have prevented the flood nor reopened the depot sooner.
Computed gold: `yes`

## contract_breach / dev / 2348c1d649e5
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
I. S had successfully delivered goods to B on four earlier occasions.
Computed gold: `yes`

## contract_breach / dev / 60fb45ff653c
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
I. S had successfully delivered goods to B on four earlier occasions.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `yes`

## contract_breach / dev / a4ae452d5b46
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
I. The units are small plastic toys.
Computed gold: `yes`

## contract_breach / dev / cf73c270a4df
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
I. The units are small plastic toys.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `yes`

## contract_breach / dev / 549f6eaa9c86
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered 40 of the 100 units by the end of 1 June and said the rest would follow later.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `no`

## contract_breach / dev / bdd06260babf
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. A similar shutdown had occurred at a depot in another country, but when the contract was signed S could not reasonably have foreseen the shutdown of this depot.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `no`

## contract_breach / dev / 66effbd0855a
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by S's own staff walking out, and S could have ended it at any time by giving an instruction to them.
Computed gold: `yes`

## contract_breach / dev / 4f1f3111788f
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a flood in the region, and S could neither have prevented the flood nor reopened the depot sooner.
Computed gold: `no`

## contract_breach / dev / 3ed56d1f1ee7
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
I. S had successfully delivered goods to B on four earlier occasions.
Computed gold: `no`

## contract_breach / dev / b3ac1f78befe
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
I. S had successfully delivered goods to B on four earlier occasions.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `no`

## contract_breach / dev / a72edd240101
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
I. The units are small plastic toys.
Computed gold: `no`

## contract_breach / dev / fffbc7e6092f
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
I. The units are small plastic toys.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
F5. The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.
Computed gold: `no`

## contract_breach / dev / 1f490eb1aefa
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
Computed gold: `undetermined`

## contract_breach / dev / 740d8bc6b095
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered all 100 units on 30 May.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
Computed gold: `no`

## contract_breach / dev / 3e32c24ce443
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered 40 of the 100 units by the end of 1 June and said the rest would follow later.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
Computed gold: `undetermined`

## contract_breach / dev / 984c20319b6e
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could reasonably have foreseen the depot shutdown.
Computed gold: `yes`

## contract_breach / dev / 2e6d2b4a5322
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. A similar shutdown had occurred at a depot in another country, but when the contract was signed S could not reasonably have foreseen the shutdown of this depot.
Computed gold: `undetermined`

## contract_breach / dev / 7ae2997a66e4
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
I. S had successfully delivered goods to B on four earlier occasions.
Computed gold: `undetermined`

## contract_breach / dev / 977d17d14aef
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
I. S had successfully delivered goods to B on four earlier occasions.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
Computed gold: `undetermined`

## contract_breach / dev / 6f4841352e61
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
I. The units are small plastic toys.
Computed gold: `undetermined`

## contract_breach / dev / 2b62207eca17
Rule: A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.
Question: Is the seller liable for breach of contract?
F1. Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.
F2. After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.
I. The units are small plastic toys.
F3. S delivered none of the units by the end of 1 June.
F4. When the contract was signed, S could not reasonably have foreseen the depot shutdown.
Computed gold: `undetermined`

## dismissal_no_notice / dev / ba478f55e000
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `yes`

## dismissal_no_notice / dev / 53d739fa50c7
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W arriving late to work twice in one month; W committed no theft, violence or fraud.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `no`

## dismissal_no_notice / dev / c49745a72a79
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till, but only 5 dollars.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `yes`

## dismissal_no_notice / dev / 9590c4d19d7f
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 21 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `no`

## dismissal_no_notice / dev / a27a8ab3b3a3
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M was away on business from 2 March until 5 March, and dismissed W on 8 March, 7 days after 1 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `yes`

## dismissal_no_notice / dev / d25e1b484f20
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. M had signed a written agreement promising W protection from dismissal without notice.
Computed gold: `no`

## dismissal_no_notice / dev / d99550393eee
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. M orally promised W protection from dismissal without notice, but M signed no document providing that protection.
Computed gold: `yes`

## dismissal_no_notice / dev / 00ab407bc190
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
I. W had worked for M for twelve years.
Computed gold: `yes`

## dismissal_no_notice / dev / e237d91db025
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
I. W had worked for M for twelve years.
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `yes`

## dismissal_no_notice / dev / 3f0836aaa65b
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
I. M's workshop has 20 employees.
Computed gold: `yes`

## dismissal_no_notice / dev / 5499b2a83749
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
I. M's workshop has 20 employees.
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
F5. W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.
Computed gold: `yes`

## dismissal_no_notice / dev / 67aba55d5fd5
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 21 March.
Computed gold: `no`

## dismissal_no_notice / dev / 57ad27669c07
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till, but only 5 dollars.
F4. M dismissed W on 21 March.
Computed gold: `no`

## dismissal_no_notice / dev / dd9271b66467
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
Computed gold: `undetermined`

## dismissal_no_notice / dev / 47549e50aa3c
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M discussed the matter with W on 4 March, but dismissed W only on 9 March, 8 days after 1 March.
Computed gold: `no`

## dismissal_no_notice / dev / 1a5ea1b8fbb1
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 21 March.
I. W had worked for M for twelve years.
Computed gold: `no`

## dismissal_no_notice / dev / 808b28778bba
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
I. W had worked for M for twelve years.
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 21 March.
Computed gold: `no`

## dismissal_no_notice / dev / 4e37916f6d5c
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 21 March.
I. M's workshop has 20 employees.
Computed gold: `no`

## dismissal_no_notice / dev / 62eccc9d8d25
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
I. M's workshop has 20 employees.
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 21 March.
Computed gold: `no`

## dismissal_no_notice / dev / d2d3403c0617
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W arriving late to work twice in one month; W committed no theft, violence or fraud.
F4. M dismissed W on 4 March.
Computed gold: `no`

## dismissal_no_notice / dev / b40328804b9b
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till, but only 5 dollars.
F4. M dismissed W on 4 March.
Computed gold: `undetermined`

## dismissal_no_notice / dev / 5d10cef29ef5
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M was away on business from 2 March until 5 March, and dismissed W on 8 March, 7 days after 1 March.
Computed gold: `undetermined`

## dismissal_no_notice / dev / 81979d3b2f7a
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
I. W had worked for M for twelve years.
Computed gold: `undetermined`

## dismissal_no_notice / dev / be5b4fd02578
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
I. W had worked for M for twelve years.
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
Computed gold: `undetermined`

## dismissal_no_notice / dev / 7fd025e30917
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
I. M's workshop has 20 employees.
Computed gold: `undetermined`

## dismissal_no_notice / dev / 2dd24ee7c804
Rule: An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.
Question: May the employer dismiss the worker without notice?
F1. Employer M runs a furniture workshop and dismissed worker W without notice.
F2. On 1 March M learned of certain conduct by W at work (the conduct in question).
I. M's workshop has 20 employees.
F3. The conduct in question was W stealing cash from the till.
F4. M dismissed W on 4 March.
Computed gold: `undetermined`

## hotel_safe / dev / 10c2ab2f4b04
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `yes`

## hotel_safe / dev / 77e0670ee9a1
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / 19717e5c7085
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The stolen watch was inside a sealed envelope with G's passport in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `yes`

## hotel_safe / dev / 828e15d2e176
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 3 days after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / 74179eaf4423
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the police 2 hours after discovering it and to the hotel manager 20 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `yes`

## hotel_safe / dev / 85652e7edebb
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
I. G had stayed at the Hotel Aurora on three earlier occasions.
Computed gold: `yes`

## hotel_safe / dev / f85f42289cd8
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
I. G had stayed at the Hotel Aurora on three earlier occasions.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `yes`

## hotel_safe / dev / 744f5aaa6539
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
I. The hotel lobby has a large green carpet.
Computed gold: `yes`

## hotel_safe / dev / a73a18507d9f
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
I. The hotel lobby has a large green carpet.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `yes`

## hotel_safe / dev / 8b422b60fa2b
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was in the locked wardrobe drawer in room 412, not in the hotel safe.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / dbc628b89599
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the police 2 hours after discovering it and to the hotel manager 20 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / cb7b251c7ea0
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
I. G had stayed at the Hotel Aurora on three earlier occasions.
Computed gold: `no`

## hotel_safe / dev / 5bae176bb43e
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
I. G had stayed at the Hotel Aurora on three earlier occasions.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / 8f3654c8e8b2
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
I. The hotel lobby has a large green carpet.
Computed gold: `no`

## hotel_safe / dev / 971650247874
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
I. The hotel lobby has a large green carpet.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F7. G reported the theft to the hotel manager 2 hours after discovering it.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / 58a17847127e
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `undetermined`

## hotel_safe / dev / 15eb2ed1cffe
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `no`

## hotel_safe / dev / b10cd1601e9c
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The stolen watch was inside a sealed envelope with G's passport in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `undetermined`

## hotel_safe / dev / fc3ab132d6ed
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
I. G had stayed at the Hotel Aurora on three earlier occasions.
Computed gold: `undetermined`

## hotel_safe / dev / ae3cf177fc87
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
I. G had stayed at the Hotel Aurora on three earlier occasions.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `undetermined`

## hotel_safe / dev / 4a28066812ea
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
I. The hotel lobby has a large green carpet.
Computed gold: `undetermined`

## hotel_safe / dev / 7b9860e045a6
Rule: A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).
Question: Must the hotel compensate the guest?
F1. Guest G stayed at the Hotel Aurora for six nights in room 412.
F2. The hotel has four stars and 120 rooms.
F3. G's watch was stolen during the stay.
F4. The watch that was stolen was in the hotel safe at reception at the time of the theft.
I. The hotel lobby has a large green carpet.
F5. On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.
F6. The hotel's restaurant had been fully booked that night.
F8. A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.
F9. G now asks the hotel to compensate for the stolen watch.
Computed gold: `undetermined`

## licence_revocation / dev / b6c9c3bf927e
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `yes`

## licence_revocation / dev / 1fc2be71ac97
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found no safety violation at R in the March inspection.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / 603292ca6ad1
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `yes`

## licence_revocation / dev / f749bb0cf0c0
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 13 April.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / f404a2c503df
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R started the work listed in the city's notice on 10 April but completed all of it only on 5 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `yes`

## licence_revocation / dev / 5f7c96226257
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
I. R's owner has run two other restaurants in the city.
Computed gold: `yes`

## licence_revocation / dev / 6f9d54d42210
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
I. R's owner has run two other restaurants in the city.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `yes`

## licence_revocation / dev / cee8ff3803ec
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
I. R's dining room has twelve tables.
Computed gold: `yes`

## licence_revocation / dev / 44ec159b070d
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
I. R's dining room has twelve tables.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 15 June.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `yes`

## licence_revocation / dev / 9a0034cc01da
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 13 April.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / 87e4572e79f8
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 1 May, the 30th day after receiving it.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / 4e85035dae6e
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 13 April.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
I. R's owner has run two other restaurants in the city.
Computed gold: `no`

## licence_revocation / dev / 3b4a31eb01df
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
I. R's owner has run two other restaurants in the city.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 13 April.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / a869cb127387
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 13 April.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
I. R's dining room has twelve tables.
Computed gold: `no`

## licence_revocation / dev / 26de426917e8
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
I. R's dining room has twelve tables.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F7. R completed all the work listed in the city's notice on 13 April.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / 6980969c278d
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `undetermined`

## licence_revocation / dev / 8731c11fe336
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found no safety violation at R in the March inspection.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `no`

## licence_revocation / dev / 968bccee4b46
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `undetermined`

## licence_revocation / dev / ed2ffcb09b69
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
I. R's owner has run two other restaurants in the city.
Computed gold: `undetermined`

## licence_revocation / dev / 3bbc8a9ed851
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
I. R's owner has run two other restaurants in the city.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `undetermined`

## licence_revocation / dev / 1300911f9729
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
I. R's dining room has twelve tables.
Computed gold: `undetermined`

## licence_revocation / dev / 64beb68f28b9
Rule: A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).
Question: May the city revoke the restaurant's licence?
F1. Restaurant R has operated in the city centre for nine years.
F2. R employs 14 staff and serves about 200 meals per day.
F3. In March the city's food-safety office carried out an inspection of R.
F4. The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.
I. R's dining room has twelve tables.
F5. The inspector also praised R's menu labelling.
F6. On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.
F8. R's owner has since applied to extend the opening hours.
F9. The city now considers revoking R's licence.
Computed gold: `undetermined`

## protected_tenant / dev / f0c0e3b50544
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is not a protected tenant.
Computed gold: `yes`

## protected_tenant / dev / 68782ecc909e
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L never gave T any termination notice.
F3. T is not a protected tenant.
Computed gold: `no`

## protected_tenant / dev / 82ccf7fb7eaa
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L e-mailed T a termination notice, which T opened and read.
F3. T is not a protected tenant.
Computed gold: `yes`

## protected_tenant / dev / ab39b0096611
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
Computed gold: `undetermined`

## protected_tenant / dev / 358b55be8d02
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T applied to become a protected tenant, but the application has not been approved, so T is not a protected tenant.
Computed gold: `yes`

## protected_tenant / dev / 37708587fc6b
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is not a protected tenant.
I. L raised T's rent by 5 percent last year.
Computed gold: `yes`

## protected_tenant / dev / 27b96e893d38
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
I. L raised T's rent by 5 percent last year.
F2. L gave T a written termination notice.
F3. T is not a protected tenant.
Computed gold: `yes`

## protected_tenant / dev / 6ff34a1b81a4
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is not a protected tenant.
I. The flat has a balcony facing north.
Computed gold: `yes`

## protected_tenant / dev / 0d5f339d176e
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
I. The flat has a balcony facing north.
F2. L gave T a written termination notice.
F3. T is not a protected tenant.
Computed gold: `yes`

## protected_tenant / dev / ee121466aa1d
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
F4. T owes 1 month of unpaid rent.
Computed gold: `no`

## protected_tenant / dev / b44026bb214c
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L e-mailed T a termination notice, which T opened and read.
F3. T is a protected tenant.
F4. T owes 1 month of unpaid rent.
Computed gold: `no`

## protected_tenant / dev / 9f90907a617f
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is not a protected tenant.
F4. T owes 1 month of unpaid rent.
Computed gold: `yes`

## protected_tenant / dev / fa45470aedee
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T has been a protected tenant since the start of the tenancy, five years ago.
F4. T owes 1 month of unpaid rent.
Computed gold: `no`

## protected_tenant / dev / a4bbfe03dca7
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
F4. T owes 3 months of unpaid rent.
Computed gold: `yes`

## protected_tenant / dev / 1e03e6f1aeab
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
F4. T owes unpaid rent for exactly 2 months.
Computed gold: `no`

## protected_tenant / dev / 496097d84e48
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
F4. T owes 1 month of unpaid rent.
I. L raised T's rent by 5 percent last year.
Computed gold: `no`

## protected_tenant / dev / c25e6c64d9f4
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
I. L raised T's rent by 5 percent last year.
F3. T is a protected tenant.
F4. T owes 1 month of unpaid rent.
Computed gold: `no`

## protected_tenant / dev / c88d0b24e17c
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
F4. T owes 1 month of unpaid rent.
I. The flat has a balcony facing north.
Computed gold: `no`

## protected_tenant / dev / 7f1d2108d49e
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
I. The flat has a balcony facing north.
F3. T is a protected tenant.
F4. T owes 1 month of unpaid rent.
Computed gold: `no`

## protected_tenant / dev / 5d9716212aa2
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L never gave T any termination notice.
F3. T is a protected tenant.
Computed gold: `no`

## protected_tenant / dev / fef35326fcc1
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L e-mailed T a termination notice, which T opened and read.
F3. T is a protected tenant.
Computed gold: `undetermined`

## protected_tenant / dev / 630d026bb0fe
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T has been a protected tenant since the start of the tenancy, five years ago.
Computed gold: `undetermined`

## protected_tenant / dev / 1c9fe2d25518
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
I. L raised T's rent by 5 percent last year.
Computed gold: `undetermined`

## protected_tenant / dev / f2cc98dcaada
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
I. L raised T's rent by 5 percent last year.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
Computed gold: `undetermined`

## protected_tenant / dev / 1ad4c3bd0b19
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
I. The flat has a balcony facing north.
Computed gold: `undetermined`

## protected_tenant / dev / 29684b7ada5b
Rule: A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.
Question: Must the tenant vacate the flat?
F1. Tenant T rents a flat from landlord L.
I. The flat has a balcony facing north.
F2. L gave T a written termination notice.
F3. T is a protected tenant.
Computed gold: `undetermined`

## severance_pay / dev / bd9f4cc47955
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `yes`

## severance_pay / dev / 32462aa8fc79
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer did not dismiss E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `no`

## severance_pay / dev / 53feab5300cb
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign, and the employer dismissed E the next day.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `yes`

## severance_pay / dev / 2870f3a130b4
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 8 months.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `no`

## severance_pay / dev / 5cf509c1a399
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for exactly 2 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `yes`

## severance_pay / dev / 0f74452bdc43
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
F5. E signed nothing about severance pay.
Computed gold: `no`

## severance_pay / dev / b082c06885b3
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E was late to work on 6 occasions, which the employer's handbook classes as minor misconduct, and E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `yes`

## severance_pay / dev / 8700e5195582
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed a written waiver of severance pay.
Computed gold: `no`

## severance_pay / dev / cd79b628eaf5
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E said to the manager 'I do not need any severance pay', but signed nothing.
Computed gold: `yes`

## severance_pay / dev / b387d452b31c
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
I. E had received a bonus the previous year.
Computed gold: `yes`

## severance_pay / dev / ce5fe1deecf1
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
I. E had received a bonus the previous year.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `yes`

## severance_pay / dev / f5e9c1d87fa9
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
I. The logistics company has a warehouse near the airport.
Computed gold: `yes`

## severance_pay / dev / 383b3bd29da8
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
I. The logistics company has a warehouse near the airport.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
F5. E signed nothing about severance pay.
Computed gold: `yes`

## severance_pay / dev / 4377443a024b
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
Computed gold: `no`

## severance_pay / dev / 89c62a5e815e
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign, and the employer dismissed E the next day.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
Computed gold: `no`

## severance_pay / dev / 898cfdc4520e
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for exactly 2 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
Computed gold: `no`

## severance_pay / dev / 25e974083ae6
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
Computed gold: `undetermined`

## severance_pay / dev / 3ed82b683bcd
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E repeatedly threatened colleagues with violence, and the employer's written disciplinary record, made after a hearing at which E was represented, records these threats.
Computed gold: `no`

## severance_pay / dev / 1a7615e126cb
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
I. E had received a bonus the previous year.
Computed gold: `no`

## severance_pay / dev / e6b1c446290b
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
I. E had received a bonus the previous year.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
Computed gold: `no`

## severance_pay / dev / 0ee0508d9f26
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
I. The logistics company has a warehouse near the airport.
Computed gold: `no`

## severance_pay / dev / 99a3d46f9fde
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
I. The logistics company has a warehouse near the airport.
F3. E had worked for the employer for 5 years.
F4. E stole company equipment, and the employer's written disciplinary record records this theft.
Computed gold: `no`

## severance_pay / dev / 36c01a103d94
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer did not dismiss E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
Computed gold: `no`

## severance_pay / dev / 9145e9c3191f
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign, and the employer dismissed E the next day.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
Computed gold: `undetermined`

## severance_pay / dev / 19738b03b5fa
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 8 months.
F4. E committed no theft and made no threats of violence.
Computed gold: `no`

## severance_pay / dev / e2caf7afd1cb
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for exactly 2 years.
F4. E committed no theft and made no threats of violence.
Computed gold: `undetermined`

## severance_pay / dev / 37c9778e2a50
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E was late to work on 6 occasions, which the employer's handbook classes as minor misconduct, and E committed no theft and made no threats of violence.
Computed gold: `undetermined`

## severance_pay / dev / ab9a518d875d
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
I. E had received a bonus the previous year.
Computed gold: `undetermined`

## severance_pay / dev / 6b691eb9523a
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
I. E had received a bonus the previous year.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
Computed gold: `undetermined`

## severance_pay / dev / e58f7108142a
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
I. The logistics company has a warehouse near the airport.
Computed gold: `undetermined`

## severance_pay / dev / f1a4d7c895dc
Rule: An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.
Question: Is the employee entitled to severance pay?
F1. Employee E worked for a logistics company.
F2. The employer dismissed E.
I. The logistics company has a warehouse near the airport.
F3. E had worked for the employer for 5 years.
F4. E committed no theft and made no threats of violence.
Computed gold: `undetermined`

## defective_goods / dev / 96a1a02937d5
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `yes`

## defective_goods / dev / 7bc8b5038da6
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was not faulty on delivery: the machine worked perfectly when B first ran it.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / 2cb9a52f441e
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine worked on the first cycle, but its motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the motor was faulty on delivery.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `yes`

## defective_goods / dev / 580aa6078e22
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 30 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / 4f07a7703852
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S an e-mail complaining that the machine's motor was faulty on 26 May, 14 days after delivery.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `yes`

## defective_goods / dev / 2a9ab59d08d9
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / bfdf08661603
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S's website listed it as 'factory second', and S told B nothing about its motor through any channel (website, telephone, e-mail or in person).
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `yes`

## defective_goods / dev / 2bc9da98ca45
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
I. B had bought three other appliances from S without any problem.
Computed gold: `yes`

## defective_goods / dev / 33e259e0b14e
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
I. B had bought three other appliances from S without any problem.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `yes`

## defective_goods / dev / 11fc49abdf88
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
I. The machine is white and has a 7 kg drum.
Computed gold: `yes`

## defective_goods / dev / 21585f42a872
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
I. The machine is white and has a 7 kg drum.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `yes`

## defective_goods / dev / f26606f1b14a
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
F5. The machine was delivered to B's home on 12 May.
F6. The machine worked on the first cycle, but its motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the motor was faulty on delivery.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / 4dd9c4f0f2c8
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S an e-mail complaining that the machine's motor was faulty on 26 May, 14 days after delivery.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / f215bb013f05
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B by telephone that the machine's motor was faulty, and B repeated the statement back to S.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / 94d06a4d5f87
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
I. B had bought three other appliances from S without any problem.
Computed gold: `no`

## defective_goods / dev / cd85da01eeab
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
I. B had bought three other appliances from S without any problem.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / f48846b5dc34
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
I. The machine is white and has a 7 kg drum.
Computed gold: `no`

## defective_goods / dev / 44b54714817a
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
I. The machine is white and has a 7 kg drum.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F8. B sent S a message complaining that the machine's motor was faulty on 20 May.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / 301a2f9661a7
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `undetermined`

## defective_goods / dev / 28911d120a22
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was not faulty on delivery: the machine worked perfectly when B first ran it.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / 1390b5753e3b
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine worked on the first cycle, but its motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the motor was faulty on delivery.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `undetermined`

## defective_goods / dev / 012719a12290
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B in writing that the machine's motor was faulty.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `no`

## defective_goods / dev / f23defc85f21
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S's website listed it as 'factory second', and S told B nothing about its motor through any channel (website, telephone, e-mail or in person).
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `undetermined`

## defective_goods / dev / d7e10bc25176
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
I. B had bought three other appliances from S without any problem.
Computed gold: `undetermined`

## defective_goods / dev / bebab86fb6ed
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
I. B had bought three other appliances from S without any problem.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `undetermined`

## defective_goods / dev / b88534ef7d3f
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
I. The machine is white and has a 7 kg drum.
Computed gold: `undetermined`

## defective_goods / dev / 2e5e1cff6f6c
Rule: A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).
Question: May B return the machine for a refund?
F1. Buyer B ordered a washing machine from seller S through S's website on 3 May.
F2. The website listed the machine at 480 dollars and offered free installation within 10 days of delivery.
F3. S's standard warranty on all machines is 24 months.
F4. Before B bought the machine, S told B nothing about any fault in the machine's motor.
I. The machine is white and has a 7 kg drum.
F5. The machine was delivered to B's home on 12 May.
F6. The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.
F7. B's neighbour, who is an electrician, offered to help B with the installation.
F9. B has since asked S for a refund of the 480 dollars.
Computed gold: `undetermined`

## permit_renewal / test / 532a985d5b73
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `yes`

## permit_renewal / test / d049eeadd6fc
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 25 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `no`

## permit_renewal / test / e664fc6f1260
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 16 June 2026, exactly 14 days before the expiry date.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `yes`

## permit_renewal / test / 2be0537a9797
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had unpaid stall fees of 250 dollars.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `no`

## permit_renewal / test / a657a327e9a6
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. H had owed 120 dollars in stall fees in May 2026 but paid all of it on 20 June 2026, so on 30 June 2026 no stall fee was unpaid.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `yes`

## permit_renewal / test / d3a71f1d205a
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
Computed gold: `no`

## permit_renewal / test / f815008c4822
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 24 June 2025 to 30 June 2025 and at no other time.
Computed gold: `yes`

## permit_renewal / test / 406ccf0d64c9
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
I. H has held a permit at this market for nine years.
Computed gold: `yes`

## permit_renewal / test / 20fe7ec8daa3
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
I. H has held a permit at this market for nine years.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `yes`

## permit_renewal / test / c8c03fbd358e
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
I. The market's stalls are made of green canvas.
Computed gold: `yes`

## permit_renewal / test / 8d6d7820a9da
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
I. The market's stalls are made of green canvas.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office never suspended H's permit.
Computed gold: `yes`

## permit_renewal / test / 8685ba1dcc8b
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 16 June 2026, exactly 14 days before the expiry date.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
Computed gold: `no`

## permit_renewal / test / a6417d2b7854
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. H had owed 120 dollars in stall fees in May 2026 but paid all of it on 20 June 2026, so on 30 June 2026 no stall fee was unpaid.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
Computed gold: `no`

## permit_renewal / test / 289f179f74fc
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit for one day, on 1 July 2025.
Computed gold: `no`

## permit_renewal / test / 964d790d3ea5
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
I. H has held a permit at this market for nine years.
Computed gold: `no`

## permit_renewal / test / 079f7e74c9f0
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
I. H has held a permit at this market for nine years.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
Computed gold: `no`

## permit_renewal / test / 7bbfb4089737
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
I. The market's stalls are made of green canvas.
Computed gold: `no`

## permit_renewal / test / 1398f0bfa3bb
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
I. The market's stalls are made of green canvas.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
F5. The office suspended H's permit from 3 March 2026 to 10 March 2026.
Computed gold: `no`

## permit_renewal / test / 63de411ea966
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
Computed gold: `undetermined`

## permit_renewal / test / 62c69f6bb654
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 25 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
Computed gold: `no`

## permit_renewal / test / 3cf53ba9ff3d
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 16 June 2026, exactly 14 days before the expiry date.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
Computed gold: `undetermined`

## permit_renewal / test / 88c7d9e45094
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had unpaid stall fees of 250 dollars.
F4. The city office is now deciding on the renewal.
Computed gold: `no`

## permit_renewal / test / 1d10d7390e6b
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. H had owed 120 dollars in stall fees in May 2026 but paid all of it on 20 June 2026, so on 30 June 2026 no stall fee was unpaid.
F4. The city office is now deciding on the renewal.
Computed gold: `undetermined`

## permit_renewal / test / e9e1aa066e2c
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
I. H has held a permit at this market for nine years.
Computed gold: `undetermined`

## permit_renewal / test / 933123c11cb5
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
I. H has held a permit at this market for nine years.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
Computed gold: `undetermined`

## permit_renewal / test / de7a3c7bd07c
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
I. The market's stalls are made of green canvas.
Computed gold: `undetermined`

## permit_renewal / test / d158fbfb3fed
Rule: A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).
Question: Must the city office renew the permit?
F1. Stall holder H holds a market-stall permit that expires on 30 June 2026.
F2. H filed the renewal form on 10 June 2026.
I. The market's stalls are made of green canvas.
F3. On 30 June 2026, H had no unpaid stall fees.
F4. The city office is now deciding on the renewal.
Computed gold: `undetermined`

## grant_eligibility / test / 1abd292f305e
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / 4f862e60121f
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a for-profit company and was not registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `no`

## grant_eligibility / test / aba18a21fb49
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. O's non-profit registration took effect on 1 September 2026, the closing date.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / 6d89a444c8c1
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `undetermined`

## grant_eligibility / test / fc4e3f24fe97
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed exactly 2 earlier projects funded by the foundation, and a third funded project is still in progress.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / bf89882a192d
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 60,000 dollars.
Computed gold: `no`

## grant_eligibility / test / 8e4c7bd8eea2
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests exactly 50,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / 03cec7cc1b1c
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
I. The foundation's headquarters are in a different city from O's office.
Computed gold: `yes`

## grant_eligibility / test / 06f2a02aa3c4
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
I. The foundation's headquarters are in a different city from O's office.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / 26bc31eaba31
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
I. The foundation's annual report has a blue cover.
Computed gold: `yes`

## grant_eligibility / test / 497f112eec45
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
I. The foundation's annual report has a blue cover.
F3. O has completed 4 earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / e1b33b1b7ef2
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `no`

## grant_eligibility / test / 41abeacdee39
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. O's non-profit registration took effect on 1 September 2026, the closing date.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `no`

## grant_eligibility / test / dc606ebe0932
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed 4 earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `undetermined`

## grant_eligibility / test / ec6615aec31a
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed exactly 1 earlier project funded by the foundation, and 2 other funded projects are still in progress.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `no`

## grant_eligibility / test / a35369367e35
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names Northfield University as co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `undetermined`

## grant_eligibility / test / 165ea0d0fd02
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application mentions Northfield University only as the author of a letter of support, not as a co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `no`

## grant_eligibility / test / 5b556ddabbb6
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
I. The foundation's headquarters are in a different city from O's office.
Computed gold: `no`

## grant_eligibility / test / 9e78eb3655d8
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
I. The foundation's headquarters are in a different city from O's office.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `no`

## grant_eligibility / test / 6d351f1fb5c2
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
I. The foundation's annual report has a blue cover.
Computed gold: `no`

## grant_eligibility / test / ef400f1ead0a
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
I. The foundation's annual report has a blue cover.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
Computed gold: `no`

## grant_eligibility / test / 95f3cb620c1b
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a for-profit company and was not registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `no`

## grant_eligibility / test / 135765367131
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. O's non-profit registration took effect on 1 September 2026, the closing date.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `undetermined`

## grant_eligibility / test / 617b6400dcd0
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed exactly 1 earlier project funded by the foundation, and 2 other funded projects are still in progress.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `undetermined`

## grant_eligibility / test / a4e88977e433
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names Northfield University as co-applicant.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `yes`

## grant_eligibility / test / 4f1b04fb3111
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F4. The application names no co-applicant.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `no`

## grant_eligibility / test / b3dc3432e3ca
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 60,000 dollars.
Computed gold: `no`

## grant_eligibility / test / 58c4ba84049d
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests exactly 50,000 dollars.
Computed gold: `undetermined`

## grant_eligibility / test / be566d9cf6bd
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
I. The foundation's headquarters are in a different city from O's office.
Computed gold: `undetermined`

## grant_eligibility / test / fe5b70a9a5d6
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
I. The foundation's headquarters are in a different city from O's office.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `undetermined`

## grant_eligibility / test / 5cd94e4ff031
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
I. The foundation's annual report has a blue cover.
Computed gold: `undetermined`

## grant_eligibility / test / 8cc9dfd572a9
Rule: A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).
Question: Must the foundation award the grant?
F1. Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.
F2. On 1 September 2026, O was registered as a non-profit organisation.
I. The foundation's annual report has a blue cover.
F3. O has completed no earlier projects funded by the foundation.
F5. The foundation is now deciding the application.
F6. The application requests 30,000 dollars.
Computed gold: `undetermined`

## archive_access / test / 1fef6e1e742f
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `yes`

## archive_access / test / e227f09f76db
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `undetermined`

## archive_access / test / 1839012f9f56
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R's researcher card had 15 March 2026 as its last valid day.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `yes`

## archive_access / test / 50729d3f6068
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 10 May 1999.
Computed gold: `no`

## archive_access / test / 72c735391c2c
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 15 March 1996, exactly 30 years before the request date.
Computed gold: `yes`

## archive_access / test / ca8726c020b5
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
I. R is writing a book about local railways.
Computed gold: `yes`

## archive_access / test / ebf0e790d2e4
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
I. R is writing a book about local railways.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `yes`

## archive_access / test / 20bd8b6bd62e
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
I. The archive's reading room has twelve desks.
Computed gold: `yes`

## archive_access / test / 9252210d68a0
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
I. The archive's reading room has twelve desks.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `yes`

## archive_access / test / afaedfedfaf0
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
Computed gold: `no`

## archive_access / test / 3e1828d949dc
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. On 15 March 2026, R held a researcher card that was valid until 31 December 2026.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
Computed gold: `undetermined`

## archive_access / test / 8bc49021b269
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R's researcher card had expired on 14 March 2026, the day before the request date.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
Computed gold: `no`

## archive_access / test / 158ce6acd1d3
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held a letter, signed by the file's donor, giving R permission to access the file.
F4. The archivist is now deciding the request.
Computed gold: `undetermined`

## archive_access / test / 32bde671a9e5
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held a letter giving R permission to access the file, signed by the donor's lawyer and not by the donor.
F4. The archivist is now deciding the request.
Computed gold: `no`

## archive_access / test / adba8c7f2053
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
I. R is writing a book about local railways.
Computed gold: `no`

## archive_access / test / d4a4068f97ae
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
I. R is writing a book about local railways.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
Computed gold: `no`

## archive_access / test / 4ee7066539e0
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
I. The archive's reading room has twelve desks.
Computed gold: `no`

## archive_access / test / 5920211d19e2
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
I. The archive's reading room has twelve desks.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
Computed gold: `no`

## archive_access / test / 32c0e93a348c
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R's researcher card had expired on 14 March 2026, the day before the request date.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `undetermined`

## archive_access / test / 19dc94ef1e78
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held a letter, signed by the file's donor, giving R permission to access the file.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `yes`

## archive_access / test / 7c223c204eb1
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F3. R held no written permission from the file's donor.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `no`

## archive_access / test / 1885658e0009
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 10 May 1999.
Computed gold: `no`

## archive_access / test / 6236e0ecd9ce
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 15 March 1996, exactly 30 years before the request date.
Computed gold: `undetermined`

## archive_access / test / e73638134d61
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
I. R is writing a book about local railways.
Computed gold: `undetermined`

## archive_access / test / cd3558f07ecb
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
I. R is writing a book about local railways.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `undetermined`

## archive_access / test / a4691ee254ba
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
I. The archive's reading room has twelve desks.
Computed gold: `undetermined`

## archive_access / test / ac49c5f1e53e
Rule: A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).
Question: May the reader access the file?
F1. Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.
F2. R held no researcher card on 15 March 2026.
I. The archive's reading room has twelve desks.
F4. The archivist is now deciding the request.
F5. The file was closed on 2 June 1980.
Computed gold: `undetermined`

## export_certificate / test / 028ef93f3f56
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `yes`

## export_certificate / test / 9b649eb77bed
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was not registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `no`

## export_certificate / test / d93cea4a5ca8
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. X's registration with the office took effect on 4 May 2026, the application date.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `yes`

## export_certificate / test / 04fedde9df64
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 19 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `no`

## export_certificate / test / 622f049f1b91
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 15 May 2026, exactly 5 days before departure.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `yes`

## export_certificate / test / 5e173d27b40b
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `undetermined`

## export_certificate / test / 8b335f9105c1
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained a chemical whose name resembles a Category-X chemical but which is not itself a Category-X chemical.
Computed gold: `yes`

## export_certificate / test / 763e958bf4eb
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
I. X has exported goods to the same country twice before.
Computed gold: `yes`

## export_certificate / test / e1f796755b9b
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
I. X has exported goods to the same country twice before.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `yes`

## export_certificate / test / bf6387029f01
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
I. The shipment will travel by lorry.
Computed gold: `yes`

## export_certificate / test / 7120794e40e1
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
I. The shipment will travel by lorry.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
Computed gold: `yes`

## export_certificate / test / 482ac4a99684
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
Computed gold: `no`

## export_certificate / test / 3c6ed8042f07
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. X's registration with the office took effect on 4 May 2026, the application date.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
Computed gold: `no`

## export_certificate / test / aec9046a0255
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 15 May 2026, exactly 5 days before departure.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
Computed gold: `no`

## export_certificate / test / f459acde8d51
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained no Category-X chemical.
F6. The shipment's total weight was 300 kg.
Computed gold: `yes`

## export_certificate / test / 1c2b23904dfa
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained a retail-packaged cleaning product with a small amount of a Category-X chemical as one ingredient.
F6. The shipment's total weight was 300 kg.
Computed gold: `no`

## export_certificate / test / 075feb4ee710
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 60 kg.
Computed gold: `yes`

## export_certificate / test / 644853f8fed7
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 100.5 kg.
Computed gold: `no`

## export_certificate / test / cccc2316c7ae
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
I. X has exported goods to the same country twice before.
Computed gold: `no`

## export_certificate / test / 6d3f9a53aed4
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
I. X has exported goods to the same country twice before.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
Computed gold: `no`

## export_certificate / test / 360fb3a32ef0
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
I. The shipment will travel by lorry.
Computed gold: `no`

## export_certificate / test / fbefec41598b
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
I. The shipment will travel by lorry.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
F6. The shipment's total weight was 300 kg.
Computed gold: `no`

## export_certificate / test / 5780c9c7371c
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was not registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `no`

## export_certificate / test / 792ad1ac896c
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. X's registration with the office took effect on 4 May 2026, the application date.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `undetermined`

## export_certificate / test / 8918cbffa52a
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 19 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `no`

## export_certificate / test / 0f81d0d06940
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 15 May 2026, exactly 5 days before departure.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `undetermined`

## export_certificate / test / dc3bb9cf9077
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained a retail-packaged cleaning product with a small amount of a Category-X chemical as one ingredient.
Computed gold: `undetermined`

## export_certificate / test / d8b75113a8c0
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
I. X has exported goods to the same country twice before.
Computed gold: `undetermined`

## export_certificate / test / 63e953e81726
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
I. X has exported goods to the same country twice before.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `undetermined`

## export_certificate / test / 9da684722b95
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
I. The shipment will travel by lorry.
Computed gold: `undetermined`

## export_certificate / test / 272abe2d86ac
Rule: An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).
Question: Must the export office issue the certificate?
F1. Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.
F2. On 4 May 2026, X was registered with the office as an exporter.
I. The shipment will travel by lorry.
F3. The customs form was submitted on 8 May 2026.
F4. The export office is now deciding the application.
F5. The shipment contained 20 litres of a solvent that is a Category-X chemical.
Computed gold: `undetermined`
