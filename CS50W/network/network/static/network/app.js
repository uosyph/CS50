function clearEditView(postId) {
    document.getElementById(`textarea_${postId}`).remove();
    document.getElementById(`save_${postId}`).remove();
    document.getElementById(`cancel_${postId}`).remove();
    document.getElementById(`post_content_${postId}`).style.display = 'block';
    document.getElementById(`edit_${postId}`).style.display = 'inline-block';
    document.getElementById(`post_likes_${postId}`).style.display = 'block';
}

// Add validation message to parentDiv
function addValidationMessage(message, parentDiv) {
    const warningMessage = document.createElement('p');
    warningMessage.innerHTML = message;
    warningMessage.className = 'text-danger';
    document.getElementById(parentDiv).append(warningMessage);
}

// Update the number of likes for a given ID.
function updateLikes(id, likes) {
    let likeCount = document.getElementById(`post_likecount_${id}`);
    likeCount.innerHTML = likes;
}

document.addEventListener('DOMContentLoaded', function () {

    // Listen for clicks on the page
    document.addEventListener('click', event => {
        const element = event.target;

        // If the user clicked on 'like'
        if (element.id.startsWith('post_likeicon_')) {

            // Save post ID from data in element
            let id = element.dataset.id;

            // Update page without full reload
            fetch(`/updatelike/${id}`, {
                method: "POST"
            })
                .then(function (response) {
                    if (response.ok) {
                        return response.json();
                    }
                    else {
                        return Promise.reject('An error has occurred.');
                    }
                }).then(function (data) {

                    // Saving data from response
                    const likes = data.likesCount;
                    const likesPost = data.likesPost;

                    let likeIcon = document.getElementById(`post_likeicon_${id}`);

                    // Update likes
                    updateLikes(id, likes);

                    // The icon changes depending on whether the user likes the post or not
                    if (likesPost) {
                        likeIcon.className = 'likeicon likeicon-user fa-heart fas';
                    } else {
                        likeIcon.className = 'likeicon likeicon-user fa-heart far';
                    }
                }).catch(function (ex) {
                    console.log(ex);
                });
        }

        // If the user clicked on 'edit'
        if (element.id.startsWith('edit_')) {
            const editButton = element;
            const postId = editButton.dataset.id;
            const postText = document.getElementById(`post_content_${postId}`);

            // Create 'Textarea' and add it to DOM
            let textArea = document.createElement('textarea');
            textArea.innerHTML = postText.innerHTML;
            textArea.id = `textarea_${postId}`;
            textArea.className = 'form-control';
            document.getElementById(`post_contentgroup_${postId}`).append(textArea);

            // Hide content, likes, and edit button
            postText.style.display = 'none';
            document.getElementById(`post_likes_${postId}`).style.display = 'none';
            editButton.style.display = 'none';

            // Create 'Cancel' button
            const cancelButton = document.createElement('button');
            cancelButton.innerHTML = 'Cancel';
            cancelButton.className = 'btn btn-outline-danger cancel-badge badge ml-1 text-right btn-sm';
            cancelButton.id = `cancel_${postId}`;

            // Create 'Save' button
            const saveButton = document.createElement('button');
            saveButton.innerHTML = 'Save';
            saveButton.className = 'btn save-button btn-sm mt-2 px-2';
            saveButton.id = `save_${postId}`;

            // Add 'Save' button to DOM
            document.getElementById(`save_buttons_${postId}`).append(saveButton);

            // Listen for 'Cancel' button
            cancelButton.addEventListener('click', function () {
                clearEditView(postId);
            });

            // Add 'Cancel' button to DOM
            document.getElementById(`post_headline_${postId}`).append(cancelButton);

            // When a user clicks the 'Save' button, the page is updated without a full reload
            saveButton.addEventListener('click', function () {
                textArea = document.getElementById(`textarea_${postId}`);
                fetch(`/editpost/${postId}`, {
                    method: 'POST',
                    body: JSON.stringify({
                        // Update content
                        content: textArea.value,
                    })
                })
                    // handling users who don't have permission
                    .then(response => {
                        if (response.ok || response.status == 400) {
                            return response.json();
                        } else if (response.status === 404) {
                            clearEditView(postId);
                            // Hide the 'edit' button to prevent it from happening again
                            editButton.style.display = 'none';
                            addValidationMessage("You are not authorized to do this.", `post_contentgroup_${postId}`);
                            return Promise.reject('Error 404');
                        } else {
                            return Promise.reject('An error has occurred: ' + response.status);
                        }
                    })
                    .then(result => {
                        if (!result.error) {
                            // Update content in DOM
                            postText.innerHTML = result.content;
                            // Remove edit view form DOM
                            clearEditView(postId);
                        }
                        else {
                            clearEditView(postId);
                            // Hide the 'edit' button to prevent it from happening again
                            editButton.style.display = 'none';
                            addValidationMessage(result.error, `post_contentgroup_${postId}`);
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
            });
        }
    });
});