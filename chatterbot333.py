from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")


# The following loop will execute each time the user enters input
while True:
    try:
        
        user_input = input("enter something here")
        
        if user_input != "bye":
            bot_response = chatbot.get_response(user_input)

            print(bot_response)
            
        else:
             break
       

        

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

 
