import module5_mod

def main():
    number_list = module5_mod.NumberList()

    # Data initialization
    count = int(input("How many positive integers will you input? "))
    number_list.initialize_data(count)

    # Data search
    X = int(input("Enter an integer X to check if it matches your provided numbers: "))
    result = number_list.search_data(X)

    # Output results
    if result != [-1]:
        if len(result) == 1:
            print("The index of matching X:", result[0])
        else:
            print("The indices of matching X:", result)
    else:
        print(-1)

if __name__ == "__main__":
    main()