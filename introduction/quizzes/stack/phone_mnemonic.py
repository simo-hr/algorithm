from typing import List, NewType

PhoneAlphabet = NewType("PhoneAlphabet", str)


NUM_ALPHABET_MAP = {
    0: PhoneAlphabet("+"),
    1: PhoneAlphabet("@"),
    2: PhoneAlphabet("ABC"),
    3: PhoneAlphabet("DEF"),
    4: PhoneAlphabet("GHI"),
    5: PhoneAlphabet("JKL"),
    6: PhoneAlphabet("MNO"),
    7: PhoneAlphabet("PQRS"),
    8: PhoneAlphabet("TUV"),
    9: PhoneAlphabet("WXYZ"),
}


# My answer
def phone_mnemonic(phone_number: str) -> None:
    phone_number = [int(n) for n in phone_number.replace("-", "")]
    result = []
    for num in phone_number:
        chars = NUM_ALPHABET_MAP[num]
        for c in chars:
            result.append(c)


# Example answer1
def phone_mnemonic_v1(phone_number: str) -> List[str]:
    phone_number: List[int] = [int(n) for n in phone_number.replace("-", "")]
    candidate: List[PhoneAlphabet] = []
    tmp: List[PhoneAlphabet] = [""] * len(phone_number)

    def find_candidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number):
            candidate.append("".join(tmp))
        else:
            for char in NUM_ALPHABET_MAP[phone_number[digit]]:
                tmp[digit] = PhoneAlphabet(char)
                find_candidate_alphabet(digit + 1)

    find_candidate_alphabet()
    return candidate


# Example answer2
def phone_mnemonic_v2(phone_number: str) -> List[str]:
    phone_number: List[int] = [int(n) for n in phone_number.replace("-", "")]
    candidate: List[PhoneAlphabet] = []
    stack: List[PhoneAlphabet] = [""]

    while len(stack) != 0:
        alphabets = stack.pop()
        if len(alphabets) == len(phone_number):
            candidate.append(alphabets)
        else:
            for char in NUM_ALPHABET_MAP[phone_number[len(alphabets)]]:
                stack.append(PhoneAlphabet(alphabets + char))

    return candidate


if __name__ == "__main__":

    # (order_change_by_indexes("23"))
    # (order_change_by_indexes("568-379-8466"))
    # print(order_change_by_indexes("568-379-8466"))
    print(phone_mnemonic_v1("23"))
    print(phone_mnemonic_v2("23"))
