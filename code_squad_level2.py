#-*- coding: utf-8 -*-
import random
import sys

class baseball_game :
	#게임시작시 컴퓨터가 숫자 생성 후 리스트 리턴
	def random_maker():
		set_pc_list = set([])
		while len(set_pc_list) < 3 :
			ran_num=random.randrange(1,10)
			if ran_num not in set_pc_list :
				set_pc_list.add(ran_num)
		return set_pc_list		

	#입력받은 숫자를 리스트로 리턴
 	def input_change(num) :
 		user_input = num
		user_input_list = []
		user_input_list.append(int(user_input/100))
		user_input = (user_input%100)
		user_input_list.append(int(user_input/10))
		user_input = (user_input%10)
		user_input_list.append(user_input)
		return user_input_list

	#점수 리스트를 입력 받아서 메세지 출력
	def cnt_point(tmp_list):
		if (tmp_list[0] == 0) and (tmp_list[1] == 0) :
			print '낫씽'
		elif tmp_list[0] == 0 :
			print "%d 볼"%(tmp_list[1])
		elif tmp_list[1] == 0 :
			print "%d 스트라이크"%(tmp_list[0])
		else :
			print "%d 스트라이크 %d 볼"%(tmp_list[0],tmp_list[1])
		if tmp_list[0] == 3 :
			print "3개의 숫자를 모두 맞히셨습니다! 게임 종료"
			sys.exit(1) #모두 맞으면 게임 종료

	#입력한 숫자와 pc의 숫자 비교 후 점수 리턴
 	def playing(pc_list,user_input_list) :
		tmp_list =[0,0]
		for i in range(0,3) :
			if pc_list[i] == user_input_list[i] :
				tmp_list[0] += 1
			elif pc_list[i] in user_input_list :
				tmp_list[1] += 1
		return tmp_list

	pc_list=list(random_maker())

	while 1:	
		user_input=input('숫자를 입력해주세요 ex)123 : ')
		print '입력한 숫자 : %d'%(user_input)
		user_input_list=input_change(user_input)
		cnt_point(playing(pc_list,user_input_list))

test = baseball_game()

