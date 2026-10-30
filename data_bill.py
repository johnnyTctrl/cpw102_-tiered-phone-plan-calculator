def exceeds_data_limit(data_used):
    """Return true if data usage exceeds 10 GGb."""
    return data_used > 10

def get_overage_rate(data_used, has_premuim):
    """Return the correct overage rate."""
    if data_used <=10:
         return 0
    elif data_used <= 20:
        if has_premuim:
            return 1
        else:
            return 2
    else:
        if has_premuim:
            return 2
        else:
            return 3

def main():
    data_used = float(input("Enter data used (GB): "))
    base_plan_cost = float(input("Enter base monthly plan cost: "))

    premium_answer = input("Do you have premium membership? (yes or no): ")
    has_premium = premium_answer.strip().lower() == "yes"

    data_limit = 10 
    extra_data = 0
    if exceeds_data_limit(data_used):
        extra_data = data_used - data_limit
        print(f"You are {extra_data:.1f} GB over your limit.")
        if extra_data <= 5:
            print("Moderate extra usage.")
        else:
            print("High extra usage.")
    else:
        print("You are within your data limit.")

    overage_rate = get_overage_rate(data_used, has_premium)
    overage_cost = extra_data * overage_rate
    total_bill = base_plan_cost + overage_cost

    print(f"GB over limit: {extra_data:.1f}")
    if extra_data > 0:
        print(f"Overage rate: ${overage_rate:.2f} per GB")
    print(f"Overage cost: ${overage_cost:.2f}") 
    print(f"Total bill: ${total_bill:.2f}")
    if not has_premium and exceeds_data_limit(data_used):
            print("Consider premium membership to reduce ypur overage rate.")

if __name__ == "__main__":
    main()   
