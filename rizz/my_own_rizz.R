library(shiny)

rizz_quotes <- c(
  "I'm lost, can you help me? I'm looking for your number",
  "Can you help me with something? I found this girl that I want to take out but I'm not sure to where... any suggestions? [...] Cool, what time am I picking you up?",
  "Rock, paper, scissors. If I win I get your number, if you win you get mine",
  "“Excuse me. I know this is kind of weird and I'm super shy…but I was just wondering…what pick up lines work best with you?”",
  "“I don't normally do this, but you look really upset standing over here on your phone and I thought I’d offer some support…did your stocks just crash or something?” ",
  "Can you help me? There's something wrong with my phone, it doesn't have your number in it",
  "Ask for directions, 'I'm Kenny but you can call me tonight''",
  "“Do I know you from somewhere? And wow…you’re even more adorable up close.”"
)

insult_list <- c(
  "I hope that both sides of your pillow are warm tonight",
  "Are you a beaver cuz DANG you ugly",
  "You're mid anyway"
)

cheap_date_ideas <- c(
  "Bowling + Soda",
  "Mini golf + boba",
  "Painting + kiwi loco",
  "Table games + jamba juice",
  "R mountain + tropical smoothie",
  "Farmers market + yogurt",
  "Bake",
  "park walk + gelato",
  "stargazing",
  "thrift stuff + stuff"
)

expensive_list <- c(
  "heber hatchets",
  "Twin falls water fall",
  "picnic + hammocking",
  "aquarium"
)

ui <- fluidPage(
  textInput("rizzed", "Would you like to be rizzed?"),
  textInput("dateIdeas", "Do you need any date ideas?"),
  textInput("expensiveCheap", "Expensive or Cheap date?"),
  actionButton("submit", "Submit"),
  textOutput("output"),
  br(),
  textOutput("dateOutput")
)

server <- function(input, output, session) {
  choice <- reactiveVal()
  stuff <- reactiveVal()
  cheap_final <- reactiveVal()
  expensive_final <- reactiveVal()
  
  observeEvent(input$submit, {
    rizzed <- tolower(input$rizzed)
    dateIdeas <- tolower(input$dateIdeas)
    expensiveCheap <- tolower(input$expensiveCheap)
    
    choice(sample(rizz_quotes, 1))
    stuff(sample(insult_list, 1))
    cheap_final(sample(cheap_date_ideas, 1))
    expensive_final(sample(expensive_list, 1))
    
    if (rizzed != 'no') {
      output$output <- renderText({ choice() })
    } else {
      output$output <- renderText({ stuff() })
    }
    
    if (dateIdeas != 'no') {
      if (expensiveCheap == 'expensive') {
        output$dateOutput <- renderText({ expensive_final() })
      } else if (expensiveCheap == 'cheap') {
        output$dateOutput <- renderText({ cheap_final() })
      } else {
        output$dateOutput <- renderText("That's a typo, try again")
      }
    } else {
      output$dateOutput <- renderText("You're mid anyway")
    }
  })
}

shinyApp(ui, server)



