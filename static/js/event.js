$(document).ready(function () {
    $('#video-1')[0].pause();
    $('#video-2')[0].pause();
    // Video 1
    $('#video1').on('shown.bs.modal', function (event) {
        $('#video-1')[0].play();
    });
    $('#video1').on('hidden.bs.modal', function (event) {
        $('#video-1')[0].pause();
    });
    // Video 2
    $('#video2').on('shown.bs.modal', function (event) {
        $('#video-2')[0].play();
    });
    $('#video2').on('hidden.bs.modal', function (event) {
        $('#video-2')[0].pause();
    });
});
