document.addEventListener('DOMContentLoaded', () => {
    const likeForms = document.querySelectorAll('.like-form');
    const unlikeForms = document.querySelectorAll('.unlike-form');

    likeForms.forEach(likeForm => {
        likeForm.addEventListener('submit', async event => {
            event.preventDefault();
            const post_id = likeForm.getAttribute('id');
            const likeurl = likeForm.getAttribute('action');
            const csrf_token = document.querySelector('input[name=csrfmiddlewaretoken]').value;

            try {
                const response = await fetch(likeurl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrf_token,
                    },
                    body: JSON.stringify({ post_id: post_id }),
                });
                if (!response.ok) {
                    throw new Error(response.statusText);
                }

                const data = await response.json();
                console.log('like success', data);
                document.querySelector(`.like-count${post_id}`).textContent = data.likesCount;
                document.querySelector(`.unlike-count${post_id}`).textContent = data.unlikesCount;
                if (data.liked && !data.unliked) {
                    document.getElementById('thumbs-like').classList.toggle('thumbs-blue');
                    document.getElementById('like-btn').classList.remove('btn-primary');
                    document.getElementById('like-btn').classList.toggle('btn-outline-primary');
                } 
                else {
                    document.getElementById('thumbs-like').classList.remove('thumbs-blue');
                    document.getElementById('like-btn').classList.remove('btn-outline-primary');
                    document.getElementById('like-btn').classList.toggle('btn-primary');
                }
            } catch (error) {
                console.log('error', error);
            }
        });
    });
    
    unlikeForms.forEach(unlikeForm => {
        unlikeForm.addEventListener('submit', async event => {
            event.preventDefault();
            const post_id = unlikeForm.getAttribute('id');
            const unlikeurl = unlikeForm.getAttribute('action');
            const csrf_token = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    
            try {
                const response = await fetch(unlikeurl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrf_token,
                    },
                    body: JSON.stringify({ post_id: post_id }),
                });
    
                if (!response.ok) {
                    throw new Error(response.statusText);
                }
    
                const data = await response.json();
                console.log("unlike success", data);
                document.querySelector(`.unlike-count${post_id}`).textContent = data.unlikesCount;
                document.querySelector(`.like-count${post_id}`).textContent = data.likesCount;
                if (data.unliked) {
                    document.getElementById('thumbs-unlike').classList.toggle('thumbs-red');
                    document.getElementById('unlike-btn').classList.remove('btn-danger');
                    document.getElementById('unlike-btn').classList.toggle('btn-outline-danger');
                } 
                else {
                    document.getElementById('thumbs-unlike').classList.remove('thumbs-red');
                    document.getElementById('unlike-btn').classList.remove('btn-outline-danger');
                    document.getElementById('unlike-btn').classList.toggle('btn-danger');
                }
                }
            catch (error) {
                    console.log('error', error);
                }
        });
    });
});
