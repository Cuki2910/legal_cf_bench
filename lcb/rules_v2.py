"""Benchmark v2 rule set (synthetic, hand-authored, NOT yet human-audited by a second person).

Design (docs/GOLD_ADJUDICATION_v1.md, approved A01-A05 + coverage table):
  * The 15 v1 schemas keep their IDs, are INHERITED and REPAIRED here, and are all split="dev": the v1 test
    outputs were seen, so they are no longer unseen test data. origin == "v1-inherited-repaired".
  * Four NEW held-out schemas (split="test", origin == "v2-new-heldout") have IDs absent from v1.
  * No `needs`: every atom's texts are independent propositions, coherent under any T/F/absent assignment of
    the other atoms (shared referents are fixed by a neutral context sentence; no text presupposes another atom).
  * Rules are "exactly when" biconditionals; "unless E" means: if E holds the outcome does not hold.
    Thresholds, calendar counting, and "written" are stated inside the rule text. v1 files are untouched.
Gold is computed from `formula` by logic.gold (3-valued); nothing here is labelled by a model.
ponytail: single-annotator semantics; add an independent second-reader audit before any frozen run.
"""
import copy

from .rules import RULES as _V1

VERSION = "v2"
V1_IDS = tuple(r["id"] for r in _V1)

# Fields given here overwrite the v1 rule; "atoms" entries replace only the named atoms.
_REPAIRS = {
    "refund_window": dict(
        rule="A shop must refund a returned item if and only if the item was physically brought back to the shop no later than 3 days after purchase (the 3rd day counts as within 3 days). Only a physical return counts; contacting the shop about a return does not.",
        atoms=dict(A1={
            "T": ["C physically brought the jacket back to the shop 2 days after buying it.",
                  "C physically brought the jacket back to the shop 1 day after buying it, after wearing it once."],
            "F": ["C physically brought the jacket back to the shop 10 days after buying it.",
                  "C first contacted the shop about a return 2 days after buying the jacket, but physically brought the jacket back to the shop 6 days after buying it."]}),
    ),
    "noise_fine": dict(
        rule="A resident must pay a noise fine if and only if the noise was made at a clock time between 22:00 and 06:00 (the interval runs through midnight and includes both 22:00 and 06:00).",
        facts=["Resident R played loud music in R's flat on one occasion and a neighbour complained about that one occasion.", "@A1"],
    ),
    "witnessed_contract": dict(
        rule="A contract is valid if and only if at least two adults other than the contracting parties watched both parties sign it. A person who only hears the signing does not count as having watched it.",
        atoms=dict(A1={
            "T": ["Two adults, neither of whom is P or Q, watched both P and Q sign the contract.",
                  "Two adults, neither of whom is P or Q, watched both P and Q sign the contract; one of these adults is P's cousin."],
            "F": ["No adult other than P and Q watched either party sign the contract.",
                  "Exactly one adult other than P and Q watched both parties sign. A second adult heard them from another room but did not see either party sign."]}),
    ),
    "tenancy_late": dict(
        rule="A landlord may evict a tenant if and only if the tenant paid the March rent more than 30 days after its due date (exactly 30 days is not more than 30), unless the landlord accepted that payment in a notice that is both written and signed by the landlord (an oral statement is not a written notice).",
        question="May the landlord evict the tenant?",
        facts=["Landlord L rents a flat to tenant T. The March rent, due on 1 March, is the only rent payment at issue.", "@A1", "@E1"],
        atoms=dict(
            A1={"T": ["T paid the March rent 45 days after its due date.", "T paid the March rent 31 days after its due date."],
                "F": ["T paid the March rent 12 days after its due date.", "T paid the March rent exactly 30 days after its due date."]},
            E1={"T": ["L signed a written notice accepting T's payment of the March rent.",
                      "L signed a written notice that began by complaining about the delay of T's March rent payment but ended with the words 'I accept this payment of the March rent.'"],
                "F": ["L never signed any written notice about T's payment of the March rent.",
                      "L told T by phone that the timing of T's March rent payment was acceptable, but never put it in writing."]}),
    ),
    "booking_cancel": dict(
        rule="A traveller is entitled to a full refund for a cancelled hotel booking if and only if the traveller cancelled the booking at least 7 days before the check-in date (counted in calendar days; exactly 7 days counts), unless the booking was marked non-refundable at the time of booking.",
        question="Is the traveller entitled to a full refund for the cancelled booking?",
        atoms=dict(E1={
            "T": ["The booking confirmation stated 'non-refundable' at the time of booking.",
                  "At the time of booking, the small print under the price on the booking page marked this booking 'non-refundable', and V ticked the box accepting those terms."],
            "F": ["The booking was marked fully refundable at the time of booking.",
                  "The hotel's website marked the room rate as non-refundable, but V's booking, made through a travel agent, was marked refundable at the time of booking."]}),
    ),
    "minor_cancel": dict(
        rule="A signer may cancel a contract if and only if the signer was under 18 when signing it (a person who has turned 18 is not under 18), unless a parent of the signer consented to the contract in writing (an e-mail counts as writing; an oral statement does not).",
        atoms=dict(E1={
            "T": ["Z's mother signed a written consent to the contract.",
                  "Z's father wrote a short e-mail to the shop saying 'Z may buy the laptop'."],
            "F": ["No parent of Z gave any consent to the contract, written or oral.",
                  "Z's mother told Z orally 'go ahead and buy the laptop', and no parent of Z gave any written consent."]}),
        irr=["Z's uncle is a lawyer.", "The laptop is silver."],
    ),
    "debt_limitation": dict(
        rule="A debt claim is time-barred if and only if more than 10 years had passed between the due date and the filing date (counted by calendar dates; the same date 10 years later is exactly 10 years, not more), unless the debtor acknowledged the debt in writing, to anyone, between the due date and the filing date (a letter or an e-mail is writing; a spoken statement is not).",
        facts=["A debt of 5,000 dollars fell due on 1 March 2014. The creditor later filed a claim in court for the debt; the filing date is the date of that claim.", "@A1", "@E1"],
        atoms=dict(
            A1={"T": ["The creditor filed the claim on 5 May 2024.", "The creditor filed the claim on 5 March 2024."],
                "F": ["The creditor filed the claim on 5 May 2020.", "The creditor filed the claim on 28 February 2024."]},
            E1={"T": ["On 12 June 2019 the debtor sent the creditor a signed letter acknowledging the debt.",
                      "On 12 June 2019 the debtor e-mailed the creditor the sentence 'I know I still owe you the 5,000 dollars.'"],
                "F": ["Between the due date and the filing date, the debtor made no written acknowledgment of this debt to anyone.",
                      "Between the due date and the filing date, the debtor acknowledged the debt only orally in a phone call and made no written acknowledgment to anyone."]}),
    ),
    "insurance_theft": dict(
        rule="An insurer must pay a theft claim if and only if the theft happened at the insured home, unless the policyholder first reported the theft to the police more than 48 hours after discovering it (exactly 48 hours is not more than 48) and reporting it within those 48 hours was possible for the policyholder.",
        facts=["Policyholder H holds a home insurance policy on H's home (the insured home), discovered a theft, and filed a claim for it.", "@A1", "@E1", "@E2"],
        atoms=dict(
            E2={"T": ["It was possible for H to report the theft to the police within the 48 hours after discovering it.",
                      "H was busy with work, but reporting the theft to the police within those 48 hours remained possible."],
                "F": ["It was impossible for H to report the theft to the police within the 48 hours after discovering it.",
                      "H was in a remote area; no means of reporting the theft to the police was available to H during those 48 hours."]}),
    ),
    "contract_breach": dict(
        rule="A party is liable for breach of contract if and only if it failed to perform the contract (delivering all the units by the end of 1 June counts as performing), unless the failure was caused by an event that was both unforeseeable and beyond the party's control. An event is unforeseeable if, when the contract was signed, the party could not reasonably have foreseen it. An event is beyond the party's control if the party could neither have prevented it nor ended it.",
        facts=["Seller S agreed to deliver 100 units to Buyer B by the end of 1 June.",
               "After the contract was signed, the depot from which S planned to ship the units was shut down for a period (the depot shutdown). If S failed to deliver by the end of 1 June, the depot shutdown was the only cause of that failure.",
               "@A1", "@E1", "@E2"],
        atoms=dict(
            A1={"T": ["S delivered none of the units by the end of 1 June.", "S delivered 40 of the 100 units by the end of 1 June and said the rest would follow later."],
                "F": ["S delivered all 100 units on 30 May.", "S delivered all 100 units at 23:50 on 1 June, ten minutes before the end of that day."]},
            E1={"T": ["When the contract was signed, S could not reasonably have foreseen the depot shutdown.",
                      "A similar shutdown had occurred at a depot in another country, but when the contract was signed S could not reasonably have foreseen the shutdown of this depot."],
                "F": ["When the contract was signed, S could reasonably have foreseen the depot shutdown.",
                      "Shutdowns of this depot were rare, but a specific warning that S received before the contract was signed made the shutdown reasonably foreseeable."]},
            E2={"T": ["The depot shutdown was caused by a government order that S had no power to change, and S could not have prevented or ended the shutdown.",
                      "The depot shutdown was caused by a flood in the region, and S could neither have prevented the flood nor reopened the depot sooner."],
                "F": ["The depot shutdown was caused by S's own staff walking out, and S could have ended it at any time by giving an instruction to them.",
                      "The depot shutdown was caused by a third-party contractor, but S could have prevented it at any time by paying a small fee."]}),
    ),
    "dismissal_no_notice": dict(
        rule="An employer may dismiss a worker without notice if and only if the worker committed serious misconduct (theft, violence or fraud) in the conduct the employer learned of, and the employer dismissed the worker within 7 days of learning of that conduct (calendar days; day 7 counts), unless the worker was protected by a written job-protection agreement signed by the employer.",
        facts=["Employer M runs a furniture workshop and dismissed worker W without notice.",
               "On 1 March M learned of certain conduct by W at work (the conduct in question).", "@A1", "@A2", "@E1"],
        atoms=dict(
            A1={"T": ["The conduct in question was W stealing cash from the till.",
                      "The conduct in question was W stealing cash from the till, but only 5 dollars."],
                "F": ["The conduct in question was W arriving late to work twice in one month; W committed no theft, violence or fraud.",
                      "The conduct in question was W arguing loudly with a customer, but W committed no theft, violence or fraud."]},
            A2={"T": ["M dismissed W on 4 March.",
                      "M was away on business from 2 March until 5 March, and dismissed W on 8 March, 7 days after 1 March."],
                "F": ["M dismissed W on 21 March.",
                      "M discussed the matter with W on 4 March, but dismissed W only on 9 March, 8 days after 1 March."]},
            E1={"T": ["M had signed a written agreement promising W protection from dismissal without notice.",
                      "A written job-protection agreement between M and W had been signed by M and W in a ceremony attended by the whole staff, and a copy was filed with the labour office."],
                "F": ["W had no written job-protection agreement signed by M, whether in the employment contract or in any other document.",
                      "M orally promised W protection from dismissal without notice, but M signed no document providing that protection."]}),
    ),
    "hotel_safe": dict(
        rule="A hotel must compensate a guest for a stolen valuable if and only if the valuable was in the hotel safe at the time of the theft and the theft was reported to the hotel manager within 24 hours of the guest discovering it (exactly 24 hours counts as within 24 hours).",
        facts=["Guest G stayed at the Hotel Aurora for six nights in room 412.",
               "The hotel has four stars and 120 rooms.",
               "G's watch was stolen during the stay.",
               "@A1",
               "On the fifth day G travelled to a nearby town for a business meeting. When G returned in the evening, G discovered the theft of the watch.",
               "The hotel's restaurant had been fully booked that night.",
               "@A2",
               "A cleaner who had worked at the hotel for eight years was on duty on the day of the theft.",
               "G now asks the hotel to compensate for the stolen watch."],
        atoms=dict(
            A1={"T": ["The watch that was stolen was in the hotel safe at reception at the time of the theft.",
                      "The stolen watch was inside a sealed envelope with G's passport in the hotel safe at reception at the time of the theft."],
                "F": ["At the time it was stolen, the watch was on the bedside table in room 412, not in the hotel safe.",
                      "At the time it was stolen, the watch was in the locked wardrobe drawer in room 412, not in the hotel safe."]},
            A2={"T": ["G reported the theft to the hotel manager 2 hours after discovering it.",
                      "G reported the theft to the police 2 hours after discovering it and to the hotel manager 20 hours after discovering it."],
                "F": ["G reported the theft to the hotel manager 3 days after discovering it.",
                      "G reported the theft to the police 2 hours after discovering it and to the hotel manager 26 hours after discovering it."]}),
    ),
    "licence_revocation": dict(
        rule="A city may revoke a restaurant's licence if and only if the restaurant committed a safety violation found in the March inspection, unless the restaurant completed all the work listed in the city's written notice of 1 April within 30 days after receiving it (the 30th day counts; R received the notice on 1 April).",
        facts=["Restaurant R has operated in the city centre for nine years.",
               "R employs 14 staff and serves about 200 meals per day.",
               "In March the city's food-safety office carried out an inspection of R.",
               "@A1",
               "The inspector also praised R's menu labelling.",
               "On 1 April the city sent R a written notice about the March inspection, listing the work the city asked R to complete after the inspection; R received it that day.",
               "@E1",
               "R's owner has since applied to extend the opening hours.",
               "The city now considers revoking R's licence."],
        atoms=dict(
            A1={"T": ["The inspector found that R stored raw chicken above cooked food, which counts as a safety violation.",
                      "The inspector recorded a safety violation: R's fire exit was blocked by boxes, which R's owner said had been there for one hour only."],
                "F": ["The inspector found no safety violation at R in the March inspection.",
                      "The inspector found only a minor paint defect on R's dining-room wall, which is not a safety issue, so R committed no safety violation."]},
            E1={"T": ["R completed all the work listed in the city's notice on 13 April.",
                      "R completed all the work listed in the city's notice on 1 May, the 30th day after receiving it."],
                "F": ["R completed all the work listed in the city's notice on 15 June.",
                      "R started the work listed in the city's notice on 10 April but completed all of it only on 5 June."]}),
    ),
    "protected_tenant": dict(
        rule="A tenant must vacate a flat if and only if the landlord gave the tenant a written termination notice (an e-mail counts as written), unless the tenant is a protected tenant; however, that exception does not apply when the tenant owes more than 2 months of unpaid rent (exactly 2 months is not more than 2). Protected status and unpaid rent are separate facts.",
    ),
    "severance_pay": dict(
        rule="An employee is entitled to severance pay if and only if the employer dismissed the employee and the employee had worked for the employer for at least 2 years (exactly 2 years counts), unless the employee committed gross misconduct (theft or threats of violence) that is recorded in the employer's written disciplinary record, or the employee signed a written waiver of severance pay.",
        atoms=dict(
            A1={"T": ["The employer dismissed E.",
                      "The employer told E 'resign today or you will be dismissed tomorrow'; E did not resign, and the employer dismissed E the next day."],
                "F": ["The employer did not dismiss E.",
                      "The employer told E 'resign today or you will be dismissed tomorrow'; E resigned that day, and the employer never dismissed E."]},
            E1={"T": ["E stole company equipment, and the employer's written disciplinary record records this theft.",
                      "E repeatedly threatened colleagues with violence, and the employer's written disciplinary record, made after a hearing at which E was represented, records these threats."],
                "F": ["E committed no theft and made no threats of violence.",
                      "E was late to work on 6 occasions, which the employer's handbook classes as minor misconduct, and E committed no theft and made no threats of violence."]}),
    ),
    "defective_goods": dict(
        rule="A buyer may return a washing machine for a refund if and only if the machine's motor was faulty on delivery and the buyer, within 14 days after delivery (day 14 counts), sent the seller a message complaining that the motor was faulty (the complaint counts whether or not it was true), unless before the sale the seller told the buyer that the machine's motor was faulty (in writing or orally, whether or not the statement was true).",
        atoms=dict(
            A1={"T": ["The machine's motor was faulty on delivery: when B first ran the machine, the drum would not spin because of the faulty motor.",
                      "The machine worked on the first cycle, but its motor failed on the second cycle, and the repair report said the motor had been faulty since manufacture, so the motor was faulty on delivery."],
                "F": ["The machine's motor was not faulty on delivery: the machine worked perfectly when B first ran it.",
                      "The machine arrived with a scratched outer panel, but its motor was working normally on delivery."]},
            A2={"T": ["B sent S a message complaining that the machine's motor was faulty on 20 May.",
                      "B sent S an e-mail complaining that the machine's motor was faulty on 26 May, 14 days after delivery."],
                "F": ["B sent S a message complaining that the machine's motor was faulty on 30 May.",
                      "B sent S an e-mail complaining that the machine's motor was faulty on 27 May, 15 days after delivery."]},
            E1={"T": ["Before B bought the machine, S told B in writing that the machine's motor was faulty.",
                      "Before B bought the machine, S told B by telephone that the machine's motor was faulty, and B repeated the statement back to S."],
                "F": ["Before B bought the machine, S told B nothing about any fault in the machine's motor.",
                      "Before B bought the machine, S's website listed it as 'factory second', and S told B nothing about its motor through any channel (website, telephone, e-mail or in person)."]}),
    ),
}

RULES = copy.deepcopy(_V1)
for _r in RULES:
    _r.pop("needs", None)
    for _k, _v in _REPAIRS.get(_r["id"], {}).items():
        if _k == "atoms":
            _r["atoms"].update(copy.deepcopy(_v))
        else:
            _r[_k] = copy.deepcopy(_v)
    _r["split"] = "dev"  # v1 outputs were seen: inherited schemas cannot be unseen test data
    _r["origin"] = "v1-inherited-repaired"

# ---- four new held-out schemas. Every text is an independent proposition; no `needs`.
_NEW = [
    dict(
        id="permit_renewal", tier=3, split="test", override=False,
        rule="A city office must renew a market-stall permit if and only if the holder filed the renewal form no later than 14 days before the permit's expiry date (exactly 14 days counts) and the holder had no unpaid stall fees on the expiry date, unless the office suspended the permit at any time during the permit year (1 July 2025 to 30 June 2026, both dates included).",
        question="Must the city office renew the permit?",
        facts=["Stall holder H holds a market-stall permit that expires on 30 June 2026.",
               "@A1", "@A2",
               "The city office is now deciding on the renewal.",
               "@E1"],
        formula=("and", "A1", "A2", ("not", "E1")),
        atoms=dict(
            A1={"T": ["H filed the renewal form on 10 June 2026.",
                      "H filed the renewal form on 16 June 2026, exactly 14 days before the expiry date."],
                "F": ["H filed the renewal form on 25 June 2026.",
                      "H filed the renewal form on 17 June 2026, 13 days before the expiry date."]},
            A2={"T": ["On 30 June 2026, H had no unpaid stall fees.",
                      "H had owed 120 dollars in stall fees in May 2026 but paid all of it on 20 June 2026, so on 30 June 2026 no stall fee was unpaid."],
                "F": ["On 30 June 2026, H had unpaid stall fees of 250 dollars.",
                      "On 30 June 2026, H's only unpaid stall fee was 5 dollars, due since 2 June 2026."]},
            E1={"T": ["The office suspended H's permit from 3 March 2026 to 10 March 2026.",
                      "The office suspended H's permit for one day, on 1 July 2025."],
                "F": ["The office never suspended H's permit.",
                      "The office suspended H's permit from 24 June 2025 to 30 June 2025 and at no other time."]}),
        bases=dict(yes=dict(A1="T", A2="T", E1="F"), no=dict(A1="T", A2="T", E1="T"), undetermined=dict(A1="T", A2="T")),
        irr=["H has held a permit at this market for nine years.", "The market's stalls are made of green canvas."],
    ),
    dict(
        id="grant_eligibility", tier=4, split="test", override=False,
        rule="A foundation must award a research grant to an applicant if and only if the applicant was registered as a non-profit organisation on the closing date, and at least one of the following is true: the applicant has completed at least 2 earlier projects funded by the foundation, or the application names a university as co-applicant; unless the application requests more than 50,000 dollars (exactly 50,000 is not more than 50,000).",
        question="Must the foundation award the grant?",
        facts=["Organisation O applied to the Harbor Foundation for a research grant. The closing date was 1 September 2026.",
               "@A1", "@A2", "@A3",
               "The foundation is now deciding the application.",
               "@E1"],
        formula=("and", "A1", ("or", "A2", "A3"), ("not", "E1")),
        atoms=dict(
            A1={"T": ["On 1 September 2026, O was registered as a non-profit organisation.",
                      "O's non-profit registration took effect on 1 September 2026, the closing date."],
                "F": ["On 1 September 2026, O was registered as a for-profit company and was not registered as a non-profit organisation.",
                      "O's non-profit registration took effect on 2 September 2026, one day after the closing date; on 1 September 2026 O was not registered as a non-profit organisation."]},
            A2={"T": ["O has completed 4 earlier projects funded by the foundation.",
                      "O has completed exactly 2 earlier projects funded by the foundation, and a third funded project is still in progress."],
                "F": ["O has completed no earlier projects funded by the foundation.",
                      "O has completed exactly 1 earlier project funded by the foundation, and 2 other funded projects are still in progress."]},
            A3={"T": ["The application names Northfield University as co-applicant.",
                      "The application names Northfield University as co-applicant, although the university receives no money from the grant."],
                "F": ["The application names no co-applicant.",
                      "The application mentions Northfield University only as the author of a letter of support, not as a co-applicant."]},
            E1={"T": ["The application requests 60,000 dollars.",
                      "The application requests 50,001 dollars."],
                "F": ["The application requests 30,000 dollars.",
                      "The application requests exactly 50,000 dollars."]}),
        bases=dict(yes=dict(A1="T", A2="T", E1="F"), no=dict(A1="T", A2="F", A3="F"), undetermined=dict(A1="T", A2="F", E1="F")),
        irr=["The foundation's headquarters are in a different city from O's office.", "The foundation's annual report has a blue cover."],
    ),
    dict(
        id="archive_access", tier=3, split="test", override=False,
        rule="A reader may access a closed archive file if and only if, on the request date, at least one of the following is true: the reader held a valid researcher card (the card's last valid day counts as valid), or the reader held written permission signed by the file's donor; unless the file was closed fewer than 30 years before the request date (exactly 30 years is not fewer than 30).",
        question="May the reader access the file?",
        facts=["Reader R asked on 15 March 2026 to access a closed file in a city archive; 15 March 2026 is the request date.",
               "@A1", "@A2",
               "The archivist is now deciding the request.",
               "@E1"],
        formula=("and", ("or", "A1", "A2"), ("not", "E1")),
        atoms=dict(
            A1={"T": ["On 15 March 2026, R held a researcher card that was valid until 31 December 2026.",
                      "R's researcher card had 15 March 2026 as its last valid day."],
                "F": ["R held no researcher card on 15 March 2026.",
                      "R's researcher card had expired on 14 March 2026, the day before the request date."]},
            A2={"T": ["R held a letter, signed by the file's donor, giving R permission to access the file.",
                      "R held a one-line handwritten note, signed by the file's donor, saying 'R may read this file'."],
                "F": ["R held no written permission from the file's donor.",
                      "R held a letter giving R permission to access the file, signed by the donor's lawyer and not by the donor."]},
            E1={"T": ["The file was closed on 10 May 1999.",
                      "The file was closed on 16 March 1996, one day less than 30 years before the request date."],
                "F": ["The file was closed on 2 June 1980.",
                      "The file was closed on 15 March 1996, exactly 30 years before the request date."]}),
        bases=dict(yes=dict(A1="T", E1="F"), no=dict(A1="F", A2="F"), undetermined=dict(A1="F", E1="F")),
        irr=["R is writing a book about local railways.", "The archive's reading room has twelve desks."],
    ),
    dict(
        id="export_certificate", tier=4, split="test", override=False,
        rule="An export office must issue an export certificate for a shipment if and only if the exporter was registered with the office on the application date and the customs form was submitted at least 5 days before the departure date (calendar days; exactly 5 days counts), unless the shipment contained any amount of a Category-X chemical and the shipment's total weight was more than 100 kg (exactly 100 kg is not more than 100).",
        question="Must the export office issue the certificate?",
        facts=["Exporter X applied to an export office on 4 May 2026 (the application date) for a certificate for a shipment that departs on 20 May 2026.",
               "@A1", "@A2",
               "The export office is now deciding the application.",
               "@E1", "@E2"],
        formula=("and", "A1", "A2", ("not", ("and", "E1", "E2"))),
        atoms=dict(
            A1={"T": ["On 4 May 2026, X was registered with the office as an exporter.",
                      "X's registration with the office took effect on 4 May 2026, the application date."],
                "F": ["On 4 May 2026, X was not registered with the office as an exporter.",
                      "X's registration with the office took effect on 5 May 2026, the day after the application date; on 4 May 2026 X was not registered."]},
            A2={"T": ["The customs form was submitted on 8 May 2026.",
                      "The customs form was submitted on 15 May 2026, exactly 5 days before departure."],
                "F": ["The customs form was submitted on 19 May 2026.",
                      "The customs form was submitted on 16 May 2026, 4 days before departure."]},
            E1={"T": ["The shipment contained 20 litres of a solvent that is a Category-X chemical.",
                      "The shipment contained a retail-packaged cleaning product with a small amount of a Category-X chemical as one ingredient."],
                "F": ["The shipment contained no Category-X chemical.",
                      "The shipment contained a chemical whose name resembles a Category-X chemical but which is not itself a Category-X chemical."]},
            E2={"T": ["The shipment's total weight was 300 kg.",
                      "The shipment's total weight was 100.5 kg."],
                "F": ["The shipment's total weight was 60 kg.",
                      "The shipment's total weight was exactly 100 kg."]}),
        bases=dict(yes=dict(A1="T", A2="T", E1="F"), no=dict(A1="T", A2="T", E1="T", E2="T"), undetermined=dict(A1="T", A2="T", E1="T")),
        irr=["X has exported goods to the same country twice before.", "The shipment will travel by lorry."],
    ),
]
for _r in _NEW:
    _r["origin"] = "v2-new-heldout"
RULES += _NEW

assert len({r["id"] for r in RULES}) == len(RULES)
assert all(not r.get("needs") for r in RULES)
assert all(r["split"] == "dev" for r in RULES if r["id"] in V1_IDS)
assert all(r["split"] == "test" and r["id"] not in V1_IDS for r in _NEW)
