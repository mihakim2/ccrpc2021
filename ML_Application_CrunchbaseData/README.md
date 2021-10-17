
Project Introduction¶
My intention in this project is to explore the data available on Crunchbase.com, a famous enterprise data website for reporting metrics on companies including startups globally. The website releases its own rankings known as CB Rank (crunchbase rank).

Flying Kites

The Crunchbase Rank algorithm takes many signals into account including the number of connections a profile has, the level of community engagement, funding events, news articles, and acquisitions.

A company’s Rank is fluid and subject to rising and decaying over time with time-sensitive events. Events such as product launches, funding events, leadership changes, and news affect a company’s Crunchbase Rank. Crunchbase Rank is determined by an algorithm that takes into account the number of connections of a profile within the platform, the amount of community engagement, funding events, news articles, acquisitions, and more. These factors decay over time at varying rates depending on the factor (i.e., news decays more quickly than size of funding rounds).

In this analysis I am trying to identify any possible relatonship between the nature of the company ie either Tech or Non -Tech and its relationship with the CB Rank of the company, its patents, trademarks, articles, total number of investors, its active tech count or overall trend score. While Rank shows context, Crunchbase Trend Score demonstrates activity. A company’s rank will change based on activity (fundraising, news, etc.) and Trend Score is an indicator of how much their rank is changing at any given time. In other words I will use the power of Machine Learning (ML) to predict the nature of a company(ie if it is Tech company or a Non-Tech copmpany) based on available information on these data points.
