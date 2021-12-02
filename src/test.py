from xoroshiro import Xoroshiro
import calc

def main():

    prng = Xoroshiro()

    s0, s1 = prng.get_state()
    expected = (s0<<64)|s1
    observed = [prng.next()%2 for _ in range(128)]
    s = calc.getS()
    state_lst = calc.gauss_jordan(s, observed)
    state = calc.list2bitvec(state_lst)
    print(f"expected:{hex(expected)}")
    print(f"result:{hex(state)}")

if __name__ == "__main__":
    main()
    