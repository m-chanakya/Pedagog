from __future__ import unicode_literals

from django.db import models

class Forum(models.Model):
	title = models.CharField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	description = models.TextField(blank = True)


class Topic(models.Model):
	forum = models.ForeignKey(Forum, related_name = 'topics')
	title = models.CharField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	description = models.TextField(blank = True)


class Conversation(models.Model):
	topic = models.ForeignKey(Topic, related_name = 'conversations')
	title = models.CharField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	description = models.TextField(blank = True)
	creator = models.ForeignKey(User, related_name = "created_conversations")


class ConversationFollow(models.Model):
	conv = models.ForeignKey(Conversation, related_name = "followers")
	user = models.ForeignKey(User, related_name = "conversations")


class Question(models.Model):
	conv = models.ForeignKey(Conversation, related_name = "questions")
	question = models.CharField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	description = models.TextField(blank = True)
	author = models.ForeignKey(User, related_name = "asked_questions")


class QuestionFollow(models.Model):
	ques = models.ForeignKey(Question, related_name = "followers")
	user = models.ForeignKey(User, related_name = "followed_questions")


class QuestionLike(models.Model):
	ques = models.ForeignKey(Question, related_name = "likes")
	created = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, related_name = "liked_questions")


class QuestionAbuse(models.Model):
	ques = models.ForeignKey(Question, related_name = "abuses")
	created = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, related_name = "abuse_marked_questions")


class QuestionDuplicate(models.Model):
	src_ques = models.ForeignKey(Question)
	tgt_ques = models.ForeignKey(Question)
	created = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, related_name = "dup_marked_questions")


class Answer(models.Model):
	ques = models.ForeignKey(Question, related_name = "answers")
	answer = models.TextField(blank = True)
	created = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, related_name = "answered_questions")


class AnswerLike(models.Model):
	ans = models.ForeignKey(Answer, related_name = "likes")
	created = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, related_name = "liked_answers")


class AnswerAbuse(models.Model):
	ans = models.ForeignKey(Answer, related_name = "abuses")
	created = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, related_name = "abuse_marked_answers")