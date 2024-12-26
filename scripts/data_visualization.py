
import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_premium_distribution(df):
    """Plot the distribution of Total Premium."""
    plt.figure(figsize=(10, 5))
    df['TotalPremium'].hist(bins=30)
    plt.title('Distribution of Total Premium')
    plt.xlabel('Total Premium')
    plt.ylabel('Frequency')
    plt.show()

def plot_cover_type_count(df):
    """Plot the count of Cover Types."""
    plt.figure(figsize=(15,10))
    sns.countplot(x='CoverType', data=df)
    plt.title('Count of Cover Types')
    plt.show()
