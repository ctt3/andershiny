library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

  # Application title
  titlePanel("Charlie Thiry's Random Forest"),

  # Sidebar with a slider input for the image
  sidebarLayout(
    sidebarPanel(
      sliderInput("n",
                  "Image:",
                  min = 1000,
                  max = 1049,
                  value = 1000)
    ),

    # Show the image
    mainPanel(
      plotOutput("preImage"),
      h3(textOutput("prediction"))
    )
  )
))