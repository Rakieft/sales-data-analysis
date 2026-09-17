import pandas as pd
import matplotlib.pyplot as plt


def load_data(path):
    """Load the sales CSV and convert Order Date from text into a real date."""
    df = pd.read_csv(path)
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    return df


def question_top_category(df):
    """Question 1: which product category has the highest total sales?

    Groups every transaction by Item Type and sums the Total Revenue
    column for each group, then sorts the totals from highest to lowest.
    """
    revenue_by_category = df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False)
    top_category = revenue_by_category.index[0]
    top_revenue = revenue_by_category.iloc[0]

    print("Question 1: Which product category has the highest total sales?")
    print(revenue_by_category)
    print(f"Answer: {top_category} has the highest total sales, with ${top_revenue:,.2f} in revenue.\n")

    return revenue_by_category


def question_top_day(df):
    """Question 2: which day of the week has the highest number of orders?

    Extracts the day name from Order Date and counts how many orders
    fall on each day of the week.
    """
    df["Order Day"] = df["Order Date"].dt.day_name()
    orders_by_day = df["Order Day"].value_counts()
    top_day = orders_by_day.index[0]
    top_count = orders_by_day.iloc[0]

    print("Question 2: Which day of the week has the highest number of sales transactions?")
    print(orders_by_day)
    print(f"Answer: {top_day} has the most orders, with {top_count} transactions.\n")

    return orders_by_day


def question_avg_shipping_time(df):
    """Question 3: which sales channel ships orders the fastest on average?

    Converts the difference between Ship Date and Order Date into a
    number of days, then averages that per sales channel.
    """
    df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
    avg_shipping_by_channel = df.groupby("Sales Channel")["Shipping Days"].mean().sort_values()
    fastest_channel = avg_shipping_by_channel.index[0]
    fastest_avg = avg_shipping_by_channel.iloc[0]

    print("Question 3: Which sales channel ships orders the fastest on average?")
    print(avg_shipping_by_channel)
    print(f"Answer: {fastest_channel} orders ship fastest, averaging {fastest_avg:.1f} days.\n")

    return avg_shipping_by_channel


def plot_revenue_by_category(revenue_by_category, output_path):
    """Save a bar chart comparing total revenue across product categories."""
    plt.figure(figsize=(10, 6))
    revenue_by_category.plot(kind="bar", color="steelblue")
    plt.title("Total Revenue by Product Category")
    plt.xlabel("Item Type")
    plt.ylabel("Total Revenue ($)")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Graph saved as {output_path}")


def write_summary_report(revenue_by_category, orders_by_day, avg_shipping_by_channel, output_path):
    """Write a plain-text summary of all three findings to a report file.

    This gives a permanent record of the analysis results that does not
    require re-running the program to see the final answers.
    """
    top_category = revenue_by_category.index[0]
    top_revenue = revenue_by_category.iloc[0]
    top_day = orders_by_day.index[0]
    top_day_count = orders_by_day.iloc[0]
    fastest_channel = avg_shipping_by_channel.index[0]
    fastest_avg = avg_shipping_by_channel.iloc[0]

    with open(output_path, "w") as report:
        report.write("Sales Data Analysis - Summary Report\n")
        report.write("=====================================\n\n")
        report.write(f"Q1: Top product category by revenue -> {top_category} (${top_revenue:,.2f})\n")
        report.write(f"Q2: Day with the most orders -> {top_day} ({top_day_count} orders)\n")
        report.write(f"Q3: Fastest shipping sales channel -> {fastest_channel} ({fastest_avg:.1f} days average)\n")

    print(f"Summary report written to {output_path}")


def main():
    df = load_data("data/sales_data.csv")

    revenue_by_category = question_top_category(df)
    orders_by_day = question_top_day(df)
    avg_shipping_by_channel = question_avg_shipping_time(df)

    plot_revenue_by_category(revenue_by_category, "revenue_by_category.png")
    write_summary_report(revenue_by_category, orders_by_day, avg_shipping_by_channel, "results_summary.txt")


if __name__ == "__main__":
    main()
