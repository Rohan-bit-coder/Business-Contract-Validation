import random
from faker import Faker

fake = Faker()


def generate_contract():
    parties = f"This agreement is made between {fake.company()} (hereinafter referred to as 'Party A') and {fake.company()} (hereinafter referred to as 'Party B')."
    agreement_terms = f"The agreement will commence on {fake.date_this_year()} and will continue until {fake.date_this_year()}."
    confidentiality_clause = "Both parties agree to keep confidential any proprietary information disclosed."
    termination_conditions = f"This agreement may be terminated by either party upon {random.randint(30, 90)} days' written notice."
    liability_statement = "Neither party shall be liable for any indirect, incidental, or consequential damages."

    contract = f"{parties}\n\n{agreement_terms}\n\n{confidentiality_clause}\n\n{termination_conditions}\n\n{liability_statement}"
    return contract


def generate_contracts(num_contracts):
    contracts = []
    for _ in range(num_contracts):
        contracts.append(generate_contract())
    return contracts


if __name__ == "__main__":
    contracts = generate_contracts(5)
    for i, contract in enumerate(contracts):
        with open(f"contract_{i + 1}.txt", "w") as file:
            file.write(contract)
