library(shiny)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {

  output$preImage <- renderImage({
    # When input$n is 3, filename is ./images/image3.jpeg
    filename <- normalizePath(file.path('./images',
                              paste(input$n, '.png', sep='')))
 
    # Return a list containing the filename and alt text
    list(src = filename,
         alt = paste("Image number", input$n),
         width = 400,
         height = 300)

  }, deleteFile = FALSE)
  
  output$prediction <- renderText({ 
      
      paste("Prediction: ", system2("python", args=c("predict_image.py", input$n), stdout=TRUE)) 
  
  })
})