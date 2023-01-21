$(document).ready(function() {
    $('.like-form').submit(function(event) {
        event.preventDefault();
        const post_id = $(this).attr('id')
        const url = $(this).attr('action')
        console.log(url);

        $.ajax({
          type: "POST",
          url: url,
          data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 'post_id': post_id},
          success: function(data) {
            console.log("like success", data)
            $(`.like-count${post_id}`).text(data.likesCount)
            $(`.unlike-count${post_id}`).text(data.unlikesCount)
            if (data.liked && !data.unliked) {
              document.getElementById('thumbs-like').classList.toggle('thumbs-blue')
              document.getElementById('like-btn').classList.remove('btn-primary')
              document.getElementById('like-btn').classList.toggle('btn-outline-primary')
            } 
            else {
              document.getElementById('thumbs-like').classList.remove('thumbs-blue')
              document.getElementById('like-btn').classList.remove('btn-outline-primary')
              document.getElementById('like-btn').classList.toggle('btn-primary')
              
            }
          },
          error: function(response) {
            console.log('error', response)
          }
        })
    });

    $('.unlike-form').submit(function(event) {
        event.preventDefault();
        const post_id = $(this).attr('id')
        const url = $(this).attr('action')

        $.ajax({
          type: "POST",
          url: url,
          data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 'post_id': post_id},
          success: function(data) {
            console.log("unlike success", data)
            $(`.unlike-count${post_id}`).text(data.unlikesCount)
            $(`.like-count${post_id}`).text(data.likesCount)
            if (data.unliked) {
              document.getElementById('thumbs-unlike').classList.toggle('thumbs-red')
              document.getElementById('unlike-btn').classList.remove('btn-danger')
              document.getElementById('unlike-btn').classList.toggle('btn-outline-danger')
            } 
            else {
              document.getElementById('thumbs-unlike').classList.remove('thumbs-red')
              document.getElementById('unlike-btn').classList.remove('btn-outline-danger')
              document.getElementById('unlike-btn').classList.toggle('btn-danger')
            }
          },
          error: function(response) {
            console.log('error', response)
          }
        })
    });
});