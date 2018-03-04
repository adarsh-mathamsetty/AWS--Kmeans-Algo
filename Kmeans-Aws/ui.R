myData <- read.csv("quakesmr.csv")


shinyUI(pageWithSidebar(
  headerPanel('k-means clustering'),
  
  sidebarPanel(
    selectInput('xcol', 'X Variable', names(myData)),
    selectInput('ycol', 'Y Variable', names(myData),
                selected=names(myData)[[2]]),
    numericInput('clusters', 'Cluster count', 0,
                 min = 1, max = 30),
    checkboxInput('header', 'No of Clusters', FALSE)     
  ),
  mainPanel(
    plotOutput('plot1')
  )
))

