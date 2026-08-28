# Mathematical_Statistics
Study notes on mathematical statistics for data science

# 1. Probability and distributions
### 1.1. Probability
- Random variable: a variable whose value is determined probabilistically (e.g., in the coin-toss example, which face is up when the coin is tossed)
- Probability distribution: a table/figure/functional expression listing all the values a random variable can take and the probability with which those values appear (e.g., in the coin-toss example, the function telling us the probability that the upper face is heads (tails))
- Probability: a value expressing, as a number between 0 and 1, the possibility that some event has occurred (e.g., in the coin-toss example, the value of the possibility that the random variable is heads (tails))
- Event: the set of outcomes that can be observed from a random variable
- Sample space: the set of all possible events
- In P(X = head) = p, P is the probability distribution, X is the random variable, head is the event, and p is the probability

### 1.2. Probability distribution
- Uniform distribution: a distribution whose probability is the same regardless of what the event is
- Bernoulli distribution: a distribution in which the random variable X takes two values (0 or 1) → it can handle a great many problems involving a two-outcome trial, such as survival/death or good/defective
  - <img width="392" alt="screenshot 2024-05-09 9:27:33 AM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/9fc2194b-100a-444d-a380-2394de9c1300">
  - "P(X = x)": the probability that the random variable X takes the value x (for example, 1)
  - The p after ";" means that p is given as a parameter
    - Parameter of a probability distribution: a number expressing a characteristic of the probability distribution (e.g., the probability of heads for a coin in the Bernoulli distribution; the mean and variance in the normal distribution. In statistics, parameters are always written with Greek letters)
  - "{": looking at the various cases of x separately
  - Properties
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/bebe6271-7c2e-45ff-a587-cbce8e863b79)

- Support: the set of values of the random variable x whose probability is not 0 in the probability distribution (that is, a possible event (e.g., head, tail) can become part of the support, whereas an impossible event (e.g., tossing a coin and it landing on edge, neither head nor tail) has probability 0 because it cannot occur, and therefore cannot become part of the support)

### 1.3. pmf vs pdf
- Discrete probability distribution: the probability distribution when the values of the random variable X are discrete (e.g., the Bernoulli distribution)
  - The values of a random variable defined on a discrete sample space are finite or countably infinite
  - Types: Bernoulli distribution, binomial distribution, geometric distribution, multinomial distribution, Poisson distribution
- Continuous probability distribution: the probability distribution when the values of the random variable X are continuous (e.g., the continuous uniform distribution)
  - The values of the random variable are infinite and uncountable
  - Integration is used to obtain the area when computing the probability value of a continuous random variable (e.g., below is the expression solving the continuous uniform distribution)
  - Types: uniform distribution, normal distribution, chi-squared distribution, t-distribution, F distribution
  - Probability mass function (pmf) of the binomial distribution
    - <img width="400" alt="screenshot 2024-05-09 9:44:26 AM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/d3339e40-1459-4dca-9aa8-e66deac260b4">

- Probability mass function: the probability function for a discrete probability distribution, assigning a probability to each of the values x1, ..., xn of the discrete random variable X
- Probability density function: the probability function for a continuous probability distribution; the random variable X takes all values in some interval [l, u], and f(x) is the function on that interval
  - In a probability density function, X takes arbitrary real values within the given range (sample space)

### 1.4. Normal distribution
- Normal distribution: one of the continuous probability distributions, and a distribution commonly seen in nature. The Gaussian distribution
  - Characteristics: symmetric and bell shaped
- CLT (Central Limit Theorem): the theorem that the distribution of the sample mean follows a normal distribution
- Standard normal distribution (Z-distribution): a normal distribution with mean 0 and standard deviation 1
  - Every normal distribution can be transformed into the standard normal distribution.
  - The process of transforming an arbitrary normal distribution into the standard normal distribution
    1. Write a normal distribution with mean μ and variance σ² as follows: X ~ Normal(μ, σ²)
    2. Y(Z-score) = (X - μ) / σ
    3. Y ~ Normal(0, 1)

### 1.5. Binomial distribution
- Binomial distribution: the distribution extending the Bernoulli distribution, which handled success/failure in a single trial, to n trials. That is, the sum of n Bernoulli trials
  - <img width="481" alt="screenshot 2024-05-09 11:10:12 AM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/f69988f6-e76e-41a1-8edd-7422a00af3e3">
  - First term: the combination; second term: the number of successes x; third term: the number of failures, n-x
  - Mean of the binomial distribution: np, variance: np(1-p)
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/fe9169ee-52f9-4823-8710-0a74d48a87fc)
    - With n fixed, the variance grows as p approaches 0 or 1, and the variance is minimized when p is 0.5

- Multinomial distribution: binomial distribution (0 or 1) → multinomial distribution (n1, n2, n3, ...)

- Parameter space: the space in which a parameter can take meaningful values
  - Parameter space of the binomial distribution: n is an integer greater than or equal to 1, and p is a real number between 0 and 1
  - Parameter space of the normal distribution: the mean is any real value, and the variance is a real number greater than 0

### 1.6. Poisson distribution
- Poisson distribution: the probability distribution for "the number of occurrences of an event within a unit of time/space" (e.g., how many purchases occurred in one hour)
  - <img width="354" alt="screenshot 2024-05-09 11:25:00 AM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/4239e79d-c65d-42bb-b632-b6d07930821d">
  - Characteristic: both the mean and the variance are the same parameter λ
    - When doing Poisson-related modelling on real data, overdispersion is often present, and the negative binomial distribution is sometimes used to deal with it
    - Overdispersion: the case where the variance is larger than the mean
  - The Poisson distribution can also be derived from the binomial distribution. When n is very large and p is small in a binomial distribution, it can be approximated by a Poisson with λ = np
    - A representative example: the number of typographical errors that can appear on one page of a book
    - Among a great many characters (n is large), the number of typos is very small (p is small). From the Poisson viewpoint, each page can be regarded as a unit of space and the number of typos per page can be regarded as following a Poisson

### 1.7. Standardization and Normalization
- Scaling: adjusting the scale of numbers. The representative methods are standardization and normalization, and the shape of the data distribution is not changed
- Standardization: the transformation that sets the mean to 0 and the standard deviation to 1
  - <img width="100" alt="screenshot 2024-05-09 11:35:21 AM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/0fa9a0a0-c0f9-4c23-8c78-d5ab2158821e">

- Normalization: the transformation that sets the minimum to 0 and the maximum to 1
  - <img width="163" alt="screenshot 2024-05-09 11:35:33 AM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/0c24dc70-0136-49f1-97aa-2801d0a810f0">

### 1.8. Negative binomial distribution

# 2. Expectation, and more distributions
### 2.1. Expectation
- Expectation: the expected value is a concept generalized beyond a simple average
  - Not one particular value being predicted or estimated, but the average of the predicted values that are expected
  - That is, an average that takes the concept of a probability distribution into account
    - The probabilistic average value that determines the character of the probability distribution (the centre of mass, the balance point)
    - In the probability distribution represented by the random variable, the central tendency / the expected location (that is, the representative value expected as the centre)
  - In the end, a probabilistic weighted average taken over the random variable that carries the probability distribution

### 2.2. Independence
- Conditional probability: the probability that one event occurs under the assumption that a given event has occurred
  - <img width="200" alt="screenshot 2024-05-22 3:06:45 PM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/05572b84-dd48-4f1c-a4d5-804a00c0a32d">
  - Numerator: the meaning that event A and event B occurred simultaneously; denominator: the meaning that event B occurred
  - That is, the probability that event A and event B occurred simultaneously, given that event B occurred
- Independence: that the probability of one of the two events occurring has no effect on the probability of the other event occurring
  - Independence is about seeing, through the probability distribution, whether certain events or characteristics are related
  - <img width="140" alt="screenshot 2024-05-22 3:09:36 PM" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/4634f3f9-3db3-4b79-b691-6e391cffc191">
  - That is, if the conditional probability equals the original probability, the two events are independent
- Dependent: a relationship that is not independent

### 2.3. Sample & statistic

### 2.4. Chi-squared distribution

### 2.5. F and t distribution

### 2.6. Cumulative distribution function

### 2.7. Quantile

### 2.8. Compare means

### 2.9. Secretary problem

# 3. Point estimation and interval estimation
# 4. Hypothesis testing: t-test and ANOVA


# Practical Statistics for Data Scientists
## New 1. Exploratory data analysis (practice/Practice EDA~.ipynb)
- Exploratory data analysis: grasping the tendencies of complex data through summary statistics (mean, median, quantiles, etc.) and simple plots (box plots, scatter plots, etc.)
- Types of data
  - Numeric, continuous, integer (discrete), categorical, binary, ordinal
- Tabular data: the common way of representing data, made of rows and columns ~ in pandas this is the DataFrame structure (features are the columns, records are the rows)
  - features are used to predict outcome.
- 1. Estimates of location
  - The process of checking estimates that show roughly where the values of the data lie (central tendency)
  - Check the mean, weighted mean, median, percentiles, weighted median, trimmed mean, outliers, etc. + robustness
    - Weighted mean: the sum of the values multiplied by their weights, divided by the sum of the weights
    - Weighted median: after sorting the data, the data value at which the running sum of the weights from the top reaches the middle of the total. It can be obtained using the median() function of the wquantiles package
    - Trimmed mean: the mean of the remaining values after excluding a fixed number of extreme values ~ use the trim_mean function in scipy.stats
- 2. Estimates of variability
  - The process of checking dispersion, which shows how densely packed or how spread out the data values are. It is generally based on deviations (e.g., the mean absolute deviation)
  - Check deviation, variance, standard deviation (the square root of the variance), mean absolute deviation (Manhattan norm, L1 norm), median absolute deviation from the median (MAD), order statistics, range, percentiles, and the interquartile range (IQR)
    - Mean absolute deviation: the mean of the absolute values of the deviations from the mean (taking the mean of the deviations themselves is undesirable, because negative deviations cancel positive ones)
    - Median absolute deviation from the median: the median of the absolute values of the deviations from the median. Use the strong.scale.mad() function of the statsmodels package
    - Order statistics: statistics representing sorted (ranked) data; the most basic measure is the range
    - Range: the difference between the maximum and the minimum (maximum - minimum). The range is highly sensitive to extreme values and so is not very useful for measuring the variability of data ~ overcome this by using the interquartile range (IQR)
  - Variance, standard deviation and mean absolute deviation are all non-robust to extreme values → a robust estimate of variability is the median absolute deviation from the median (MAD)
    - Variance and standard deviation are especially sensitive to extreme values because they use squared deviations
- 3. Exploring the data distribution
  - Mainly the process of finding out how the data is distributed overall
  - Visualize using box plots, frequency tables, histograms and density plots
    - Density plot: a plot showing a histogram as a smooth curve, mainly using kernel density estimation
- 4. Exploring binary and categorical data
     - For binary data it is enough to find out what proportion an important category such as 1 accounts for - it can be visualized using a bar graph (count plot or bar plot)
     - Categorical data can usually be summarized as proportions, and is mainly obtained by classifying it into the following two cases
       - When there are only a few categories: bar graph (count plot or bar plot), pie chart
         - The bar graph is similar to the histogram; statisticians and data visualization experts rarely use pie charts, on the grounds that they are not visually effective
       - When there are many categories: mode, expected value
- 5. Correlation
  - Investigating the correlation between the predicted value and the target value, an important method of bivariate analysis, grasped using a correlation matrix or a scatter plot
    - When X taking a large value goes with Y taking a large value, and X taking a small value goes with Y taking a small value, they are said to be correlated
  - Correlation coefficient: a measure used to indicate what kind of relationship exists between numeric variables (-1 to +1)
    - The closer the absolute value is to 1 the higher the correlation, and the closer it is to 0 the less correlation there is (+ positive correlation, - negative correlation)
  - Correlation matrix: a table whose rows and columns denote variables, where each cell means the correlation between the variables of that row and column
  - Scatterplot: a plot whose x-axis and y-axis represent two different variables
- 6. Bivariate analysis & multivariate analysis
  - Hexagonal binning, contour plot, heatmap, contingency table, violin plot
  - Hexagonal binning: instead of marking the data as points, a plot that divides the data into hexagonal bins and colours each bin according to the number of records it contains (can be visualized using the hexbin() function of the pandas package)
    - A scatter plot is fine when there are few data points but is unsuitable for representing a great many rows; this method is used as a replacement
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/840efce2-0d5f-41a6-8f2f-6accbe7c5d58)

  - Contour plot: a plot using contour lines on top of a scatter plot; density increases towards the "peaks" of the contours (can be visualized using the kdeplot() function of the seaborn package)
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/14928a90-c21b-4c94-8782-d54d1667ef50)

  - Contingency table: an effective method of summarizing two categorical variables; a table recording the frequency counts by category
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/bb1e1ddc-4ca3-4ad3-bc80-32d875712b47)

  - Violin plot: a form that complements the box plot, simultaneously visualizing the density estimation result along the y-axis (can be visualized using the violinplot() function of the seaborn package)
    - Advantage: the distribution of the data, which is not visible in a box plot, can be seen (though the box plot shows extreme values and outliers more clearly)
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/eb3535c2-4a89-4528-bb52-db226627b4c9)
