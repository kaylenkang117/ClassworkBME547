def calc_square_root(n):

    try:
        from my_math_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt
        print("my_calculator module not available. Using default.")

    from warnings import warn
    warn("You are running a not so good function.")

    try:
        answer = sqrt(n)
    except TypeError:
        print("Enter something different")
    except ValueError:
        print("Do not enter a negative number")
    else:
        return answer


def main():
    print(calc_square_root(-4))


if __name__ == "__main__":
    main()
