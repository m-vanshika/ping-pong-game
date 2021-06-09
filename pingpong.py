import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("PING PONG")

rect_x=400
rect_y=580
Fps=60
rect_change_x=0

ball_x=50
ball_y=50

ball_change_x=5
ball_change_y=5
prev=2

score=0
def message_to_screen(msg,color,i):
	screen_text=font.render(msg,True,color)
	screen.blit(screen_text,[500,i])

def drawrect(screen,x,y):
	if x<=0:
		x=0
	if x>=699:
		x=699
	pygame.draw.rect(screen,(0,255,0),[x,y,100,20])

done=False
clock=pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				rect_change_x=-6
			elif event.key==pygame.K_RIGHT:
				rect_change_x=6
		else:
			rect_change_x=0
	screen.fill("black")
	rect_x+=rect_change_x
	if rect_x>699:
		rect_x=699
	if rect_x<0:
		rect_x=0

	ball_x+=ball_change_x
	ball_y+=ball_change_y

	if ball_x<0:
		ball_x=0
		ball_change_x=ball_change_x*-1
	if ball_x>785:
		ball_x=785
		ball_change_x=ball_change_x*-1
	if ball_y<0:
		ball_y=0
		ball_change_y=ball_change_y*-1
	if ball_x+15>=rect_x and ball_x<=rect_x+100 and ball_y==565:
		ball_change_y=ball_change_y*-1
		score=score+1
	if ball_y>=600-15:
		message_to_screen("GAME OVER","Red",400)
		pygame.display.update()	
		pygame.time.delay(3001)
		ball_change_y=ball_change_x=5
		ball_x=50
		ball_y=50
		score =0
		prev=2
		Fps=60
	pygame.draw.rect(screen,(255,255,255),[ball_x,ball_y,15,15])
	drawrect(screen,rect_x,rect_y)
	font=pygame.font.SysFont("Calibri",15,False,False)
	text=font.render("Score"+str(score),True,(255,255,255))
	screen.blit(text,[600,100])
	
	pygame.display.flip()
	clock.tick(Fps)
pygame.quit()