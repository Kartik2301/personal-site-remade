// function runScript() {
//     $.ajax({
//         url: 'do_something', 
//         success: function(data) {
//         }

//     });
// }


$(function () {
    var frm = $('#contactForm');
    frm.submit(function (ev) {
        $('#form_id').trigger("reset");
        $.ajax({
            type: frm.attr('method'),
            url: '/do_something',
            data: frm.serialize(),
            success: function (data) {
                $("#contactForm")[0].reset();
                alert('Thanks for reaching out, I will get back to you ASAP')
            }
        });
        ev.preventDefault();
    });
});
