import thinkstats2
import thinkplot

hist = thinkstats2.Hist([1, 2, 2, 3, 5])
thinkplot.Hist(hist)
thinkplot.Config(xlabel='value', ylabel='frequency')
thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')