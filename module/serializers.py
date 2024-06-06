from rest_framework import serializers
from .models import Module, Licence, Question

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'name', 'licence', 'created_at')
        read_only_fields = ['id', 'created_at']

class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        fields = ('id', 'name', 'description')
        read_only_fields = ['id']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'module','question_type','answerA','answerB','answerC','answerD', 'correct_answer')
        read_only_fields = ['id']
    
        def validate(self, data):
            question_type = data.get('question_type')
            answerC = data.get('answerC')
            answerD = data.get('answerD')
            correct_answer = data.get('correct_answer')

            if question_type == 'TF':
                if answerC or answerD:
                    raise serializers.ValidationError("For True/False questions, only answerA and answerB should be provided.")
                if correct_answer not in ['A', 'B']:
                    raise serializers.ValidationError("For True/False questions, the correct answer must be either 'A' or 'B'.")
            elif question_type == 'MC':
                if not all([data.get('answerA'), data.get('answerB'), data.get('answerC'), data.get('answerD')]):
                    raise serializers.ValidationError("For Multiple Choice questions, all answers (A, B, C, D) must be provided.")

            return data