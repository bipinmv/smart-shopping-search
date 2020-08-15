//var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
//var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
//var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

//if (SpeechRecognition === null) {
//  alert("Your browser doesn't support")
//} else {


function submitform() {
    document.getElementById("myForm").submit();
}

window.SpeechRecognition = window.SpeechRecognition ||
    window.webkitSpeechRecognition ||
    null;
var audiobutton = document.querySelector('#audiobtn');
var button = document.querySelector('#startbtn');
var result = document.querySelector('.result');
var output = document.querySelector('.output');
var searchbtn = document.querySelector('#audiosearch');
//var audioinput = document.querySelector('#audioquery');
var inputaudio = document.getElementById('audioquery');
var speechResult;

function testSpeech() {
    if (window.SpeechRecognition === null) {
        button.setAttribute('disabled', 'disabled');
        //searchbtn.setAttribute('disabled', 'disabled');
        alert("Your browser doesn't support this feature")
    } else {

        button.disabled = true;
        button.textContent = 'Listening...';
        output.textContent = '...';

        var recognition = new window.SpeechRecognition();
        //var speechRecognitionList = new SpeechGrammarList();
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.start();

        recognition.onresult = function(event) {
            speechResult = event.results[0][0].transcript.toLowerCase();
            output.textContent = speechResult;
            inputaudio.value = speechResult;

            if (speechResult == '') {
                result.textContent = 'Say something...';
                result.style.background = 'red';
            } else {
                result.style.background = 'lime';
            }

            console.log('Confidence: ' + event.results[0][0].confidence);
        }

        recognition.onspeechend = function() {
            recognition.stop();
            button.disabled = false;
            button.textContent = 'Start';
        }

        recognition.onerror = function(event) {
            button.disabled = false;
            button.textContent = 'Start';
            output.textContent = 'Error occurred in recognition: ' + event.error;
        }

        recognition.onaudiostart = function(event) {
            //Fired when the user agent has started to capture audio.
            console.log('SpeechRecognition.onaudiostart');
        }

        recognition.onaudioend = function(event) {
            //Fired when the user agent has finished capturing audio.
            console.log('SpeechRecognition.onaudioend');
        }

        recognition.onend = function(event) {
            //Fired when the speech recognition service has disconnected.
            if (speechResult != null && speechResult != '') {
                var auto_refresh = setInterval(submitform, 1000);
            }
            console.log('SpeechRecognition.onend');
            //searchbtn.disabled = false;
            //searchbtn.removeAttribute("disabled");
            //searchbtn.setAttribute("disabled", "false");
        }

        recognition.onnomatch = function(event) {
            //Fired when the speech recognition service returns a final result with no significant recognition. This may involve some degree of recognition, which doesn't meet or exceed the confidence threshold.
            console.log('SpeechRecognition.onnomatch');
        }

        recognition.onsoundstart = function(event) {
            //Fired when any sound — recognisable speech or not — has been detected.
            console.log('SpeechRecognition.onsoundstart');
        }

        recognition.onsoundend = function(event) {
            //Fired when any sound — recognisable speech or not — has stopped being detected.
            console.log('SpeechRecognition.onsoundend');
        }

        recognition.onspeechstart = function(event) {
            //Fired when sound that is recognised by the speech recognition service as speech has been detected.
            console.log('SpeechRecognition.onspeechstart');
        }
        recognition.onstart = function(event) {
            //Fired when the speech recognition service has begun listening to incoming audio with intent to recognize grammars associated with the current SpeechRecognition.
            console.log('SpeechRecognition.onstart');
        }
    }

}

button.addEventListener('click', testSpeech);