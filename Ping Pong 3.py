import turtle
import winsound

finestra = turtle.Screen()
finestra.title("Ping Pong Test da @NimaCode") # qua ho con il comando .title("") ho dato il nome al programma 
finestra.bgcolor("White") # qua ho il comando .bgcolor("NOME COLORE") dove mi mette il colore in background
finestra.setup(width=800, height=600) # qua ho il comando .setup(width=N Pixels, height= N Pixels) dove mi dimensiona il programma (larghezza, altezza)
finestra.tracer(0) # blocca la finestra dall'aggiornarsi 

# Musica di sottofondo
winsound.PlaySound("Allucination.wav", winsound.SND_ASYNC)

# Risultato
Risultato_A = 0
Risultato_B = 0

# Racchetta A
Racchetta_A = turtle.Turtle() # Definisco cosa è racchetta A prendendo da turtle la classe Turtle
Racchetta_A.speed(0) # velocità dell'animazione non della velocità racchetta
Racchetta_A.shape("square")
Racchetta_A.color("blue")
Racchetta_A.shapesize(stretch_wid=5, stretch_len=1) # comando per modificare le dimensioni, stretchwid moltiplica X volte 20 pixel di default  e via ...
Racchetta_A.penup()
Racchetta_A.goto(-350, 0) # Qui il goto sta per Go To cioè il punto di start della racchetta

# Racchetta B
Racchetta_B = turtle.Turtle() # Definisco cosa è racchetta A prendendo da turtle la classe Turtle
Racchetta_B.speed(0) # velocità dell'animazione non della velocità racchetta
Racchetta_B.shape("square")
Racchetta_B.color("blue")
Racchetta_B.shapesize(stretch_wid=5, stretch_len=1) # comando per modificare le dimensioni, stretchwid moltiplica X volte 20 pixel di default  e via ...
Racchetta_B.penup()
Racchetta_B.goto(350, 0) # Qui il goto sta per Go To cioè il punto di start della racchetta

# Palla
Palla = turtle.Turtle() # Definisco cosa è racchetta A prendendo da turtle la classe Turtle
Palla.speed(0) # velocità dell'animazione non della velocità racchetta
Palla.shape("circle")
Palla.color("blue")
Palla.penup()
Palla.goto(0, 0) # Qui il goto sta per Go To cioè il punto di start della racchetta
Palla.dx = 0.4
Palla.dy = 0.4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center", font=("Courier", 24, "normal"))

# Funzioni
def Racchetta_A_up():
    y = Racchetta_A.ycor() # da il turtle modulo
    y += 20
    Racchetta_A.sety(y)

def Racchetta_A_down():
    y = Racchetta_A.ycor() # da il turtle modulo
    y -= 20
    Racchetta_A.sety(y)

def Racchetta_B_up():
    y = Racchetta_B.ycor() # da il turtle modulo
    y += 20
    Racchetta_B.sety(y)

def Racchetta_B_down():
    y = Racchetta_B.ycor() # da il turtle modulo
    y -= 20
    Racchetta_B.sety(y)

#Keyboard binding
finestra.listen() #il programma finestra ascolta / sente gli input da tastiera
finestra.onkeypress(Racchetta_A_up, "w" ) #il programma finestra ogni volta che premo w grazie al comando onkeypress esegue il comando di Racchetta a up
finestra.onkeypress(Racchetta_A_down, "s" ) #il programma finestra ogni volta che premo s grazie al comando onkeypress esegue il comando di Racchetta a up
finestra.onkeypress(Racchetta_B_up, "Up" )
finestra.onkeypress(Racchetta_B_down, "Down" )

# Main game loop
while True: # comando per fare il loop (in questo caso quando è vero)
    finestra.update() # ogni volta che la il loop è True cioè vero ti aggiorna la finestra

    # Movimento Palla
    Palla.setx(Palla.xcor() + Palla.dx )
    Palla.sety(Palla.ycor() + Palla.dy )

    # Controllo del Bordo
    if Palla.ycor() > 290: # Appena la palla supera 290 di pixel di altezza
        Palla.sety(290) # Rimetti la Palla a 290 Pixel di altezza
        Palla.dy *= -1 # Moltiplica il parametro 0.4 * -1 modificando il moviemento della palla facendolo scendere

    if Palla.ycor() < -280: # Appena la palla supera 280 di pixel di altezza
        Palla.sety(-280) # Rimetti la Palla a 280 Pixel di altezza
        Palla.dy *= -1 # Moltiplica il parametro 0.4 * -1 modificando il moviemento della palla facendolo scendere

    if Palla.xcor() >390:
        Palla.goto(0, 0)
        Palla.dx *= -1
        Risultato_A +=1
        pen.clear() # Qua ogni volta che la palla soddisfa quell if cancella il risultato precedente non facendolo sovrascrivere sopra all'altro
        pen.write("Player A: {}  Player B: {}".format(Risultato_A, Risultato_B), align= "center", font=("Courier", 24, "normal"))
    
    if Palla.xcor() <-390:
        Palla.goto(0, 0)
        Palla.dx *= -1
        Risultato_B +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Risultato_A, Risultato_B), align= "center", font=("Courier", 24, "normal"))
    
    # Collisioni tra palla e racchetta
    if (Palla.xcor() > 340 and Palla.xcor() < 350) and (Palla.ycor() < Racchetta_B.ycor() + 50 and Palla.ycor() > Racchetta_B.ycor() -50 ):
        Palla.setx(340)
        Palla.dx *= -1
    
    if (Palla.xcor() < -340 and Palla.xcor() > -350) and (Palla.ycor() < Racchetta_A.ycor() + 50 and Palla.ycor() > Racchetta_A.ycor() -50 ):
        Palla.setx(-340)
        Palla.dx *= -1