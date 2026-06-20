import pytest
import datetime
from unittest.mock import patch, MagicMock
import project  # Assuming your script is named project.py

# Test for greeting function based on time
def test_greeting_morning():
    assert project.greeting(9) == "Good morning"

def test_greeting_afternoon():
    assert project.greeting(15) == "Good afternoon"

def test_greeting_evening():
    assert project.greeting(20) == "Good evening"


# Test for speak function using pyttsx3
@patch('pyttsx3.init')
def test_speak(mock_init):
    engine_mock = MagicMock()
    mock_init.return_value = engine_mock
    project.speak("Hello")
    engine_mock.say.assert_called_with("Hello")
    engine_mock.runAndWait.assert_called_once()


# Test for _time function
def test_time():
    with patch('project.datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime.datetime(2024, 1, 1, 10, 30)
        assert project._time() == datetime.datetime(2024, 1, 1, 10, 30).time()


# Test for listen function (using speech recognition)
@patch('project.sr.Recognizer.listen')
@patch('project.sr.Recognizer.recognize_google')
def test_listen(mock_recognize_google, mock_listen):
    mock_recognize_google.return_value = "hello"
    assert project.listen() == "hello"


# Test for getquote function (mocking the API request)
@patch('project.requests.get')
def test_getquote(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"content": "Life is short", "author": "Unknown"}
    mock_get.return_value = mock_response
    assert project.getquote() == '"Life is short — Unknown"'


# Test for replace_math_expressions function
def test_replace_math_expressions():
    input_text = "x² + y³ = z²"
    expected_output = "x squared + y cubed = z squared"
    assert project.replace_math_expressions(input_text) == expected_output


# Test for mrsmyle function (mocking API and recognizer)@patch('project.sr.Recognizer.listen')@patch('project.sr.Recognizer.listen')@patch('project.sr.Recognizer.listen')
@patch('project.sr.Recognizer.listen')  # Correct patch for listen
@patch('project.sr.Recognizer.recognize_google', return_value='hello')
@patch('project.genai.GenerativeModel')
def test_mrsmyle(mock_gen_model, mock_recognize_google, mock_listen):  # Added mock_listen here
    # Mock the generative AI model and recognizer
    mock_chat = MagicMock()
    mock_gen_model.return_value.start_chat.return_value = mock_chat

    project.mrsmyle(testing=True, mock_user_input='hello')  # Pass testing=True and mock_user_input
    mock_chat.send_message.assert_called_with("hello")

@patch('project.listen', return_value='exit')  # Patch listen to simulate 'exit'
def test_main(mock_listen):
    project.main(testing=True)  # Don't pass mock_request, so it calls listen()
    mock_listen.assert_called_once()  # Check that listen() was called once
