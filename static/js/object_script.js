var videoElem = document.getElementById('video')
var playButton = document.getElementById('playbutton')
var start = document.getElementById('start')
var stop = document.getElementById('stop')
var search = document.getElementById('search')
var stream
const status = document.getElementById('status')
var inputvideo = document.getElementById('objquery')

start.addEventListener("click", playVideo, false);
playButton.addEventListener("click", handlePlayButton, false);
stop.addEventListener("click", stopcamera);
//search.addEventListener("click", searchitem);
//playVideo();

async function playVideo() {
    const model = await mobilenet.load()
    const video = document.getElementById('video')
    const canvas = document.getElementById('canvas')
    const context = canvas.getContext('2d')

    const result = document.getElementById('result')

    stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: {
            facingMode: 'environment'
        }
    })
    video.srcObject = stream
        //predict()
    var myVar = setInterval(predict, 2000);
    async function predict() {

        context.drawImage(video, 0, 0, 500, 500)
        const predictions = await model.classify(canvas)
            //var arr =[`${predictions[0].className}`]
        status.innerHTML = `${predictions[0].className}`
        inputvideo.value = `${predictions[0].className}`

    }
}

function handlePlayButton() {
    if (videoElem.paused) {
        playVideo();
    } else {
        videoElem.pause();
        playButton.classList.remove("playing");
    }
}

function stopcamera() {
    //var stream2 = video.srcObject;
    //var tracks = stream2.getTracks();

    //for (var i = 0; i < tracks.length; i++) {
    //var track = tracks[i];
    //track.stop();
    //}
    stream.getTracks().forEach(function(track) {
        track.stop();
        video.srcObject = null;
        status.style.display = 'none';
    });
}