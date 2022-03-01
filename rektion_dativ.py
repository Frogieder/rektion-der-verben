from tester import Tester

artikeln = [
    ["(ich)", "mir"], 
    ["(du)", "dir"], 
    ["(er)", "ihm"], 
    ["(es)", "ihm"], 
    ["(sie)", "ihr"], 
    ["(wir)", "uns"], 
    ["(ihr)", "euch"], 
    ["(Sie)", "ihnen"],
    ["(der) Man", "dem"],
    ["(die) Frau", "der"],
    ["(das) Kind", "dem"],
    ["(die) Leute", "den"]
]

tester = Tester("data_dativ.txt", "to_learn_dativ.txt", artikeln=artikeln)

tester.test()
