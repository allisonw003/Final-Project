from logic import Question

def get_questions() -> list[Question]:
    """Return a list of Question objects containing the quiz's questions and answers."""
    questions = [
        Question("What is SpongeBob's job at the Krusty Krab?", ["Dishwasher", "Cashier", "Fry Cook", "Security"], "Fry Cook"),
        Question("Who is known as SpongeBob's pink best friend?", ["Patrick", "Sandy", "Squidward", "Bubble Buddy"], "Patrick"),
        Question("What kind of home does SpongeBob live in?", ["Boat", "Rock", "Pineapple", "Cave"], "Pineapple"),
        Question("What instrument is Squidward always playing?", ["Saxophone", "Clarinet", "Violin", "Flute"], "Clarinet"),
        Question("Which character runs the Chum Bucket?", ["Plankton", "Mr. Krabs", "Karen", "Larry"], "Plankton"),
        Question("SpongeBob has a pet snail. What's his name?", ["Speedy", "Gary", "Slimy", "Jerry"], "Gary"),
        Question("How many eyelashes does SpongeBob have?", ["6", "8", "3", "4"], "6"),
        Question("Where does SpongeBob work?", ["Krusty Krab", "Chum Bucket", "Shell Shack", "Goofy Goober's"], "Krusty Krab"),
        Question("Who yells \"STILL NO PICKLES!?\" in a classic episode?", ["Fred", "Bubble Bass", "Mr. Krabs", "Squidward"], "Bubble Bass"),
        Question("What phrase is DoodleBob known for saying?", ["Meep morp!", "LEEDLE", "Mi hoy minoy!", "MY LEG"], "Mi hoy minoy!"),
        Question("What is Sandy's full name?", ["Sandy Cheeks", "Sandy Squirrel", "Sandy Texas", "Sandy Light bulbs"], "Sandy Cheeks"),
        Question("What did Sandy fight that scared Bikini Bottom?", ["Sea Bear", "Alaskan Bull Worm", "Kraken", "Flying Dutchman"], "Alaskan Bull Worm"),
        Question("What activity do SpongeBob and Patrick love?", ["Karate", "Jellyfishing", "Clam catching", "Surfing"], "Jellyfishing"),
        Question("Who teaches boating school?", ["Mrs. Krabs", "Mrs. Puff", "Mr. Flounder", "Miss Coral"], "Mrs. Puff"),
        Question("What is SpongeBob trying to earn at boating school?", ["Trophy", "Medal", "License", "Sticker"], "License")
    ]
    return questions

#i learned how to put quotation marks with quotation marks referencing the following website
#https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks&ved=2ahUKEwiHkMXcpfOOAxVKm2oFHQ61FN4QFnoECBgQAQ&usg=AOvVaw2RLV2R9vA_2aLMaDUwPQQu
