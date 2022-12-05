document.addEventListener('DOMContentLoaded', function () {

	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', compose_email);
	document.querySelector('#compose-form').addEventListener('submit', send_mail)

	// By default, load the inbox
	load_mailbox('inbox');
});

function compose_email() {

	// Show compose view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';
	document.querySelector('#email-detail-view').style.display = 'none';

	// Clear out composition fields
	document.querySelector('#compose-recipients').value = '';
	document.querySelector('#compose-subject').value = '';
	document.querySelector('#compose-body').value = '';
}

function view_email(id) {
	fetch(`/emails/${id}`)
		.then(response => response.json())
		.then(email => {
			console.log(email);

			document.querySelector('#emails-view').style.display = 'none';
			document.querySelector('#compose-view').style.display = 'none';
			document.querySelector('#email-detail-view').style.display = 'block';

			document.querySelector('#email-detail-view').innerHTML = `
				<ul>
					<li class="list-group-item"><b>From:</b> ${email.sender}</li>
					<li class="list-group-item"><b>To:</b> ${email.recipients}</li>
					<li class="list-group-item"><b>Subject:</b> ${email.subject}</li>
					<li class="list-group-item"><b>Timestamp:</b> ${email.timestamp}</li>
					<li class="list-group-item">${email.body}</li>
				</ul>
			`;

			if (!email.read) {
				fetch(`/emails/${email.id}`, {
					method: 'PUT',
					body: JSON.stringify({
						read: true
					})
				})
			}


			const archivedBtn = document.createElement('button');
			archivedBtn.innerHTML = email.archived ? "Unarchived" : "Archived";
			archivedBtn.className = email.archived ? "btn btn-success" : "btn btn-danger";

			archivedBtn.addEventListener('click', function () {
				console.log('This element has been clicked!')
			});
			document.querySelector('#email-detail-view').append(archivedBtn);
		});
}

function load_mailbox(mailbox) {

	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'block';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-detail-view').style.display = 'none';

	// Show the mailbox name
	document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

	fetch(`/emails/${mailbox}`)
		.then(response => response.json())
		.then(email => {
			email.forEach(Email => {
				const newEmail = document.createElement('div');
				newEmail.className = 'list-group-item	'
				newEmail.innerHTML = `
					<h6>Sender: ${Email.sender}</h6>
					<h5>Subject: ${Email.subject}</h5>
					<p>${Email.timestamp}</p>
				`;

				newEmail.className = Email.read ? 'read' : 'unread';

				newEmail.addEventListener('click', function () {
					view_email(Email.id)
				});
				document.querySelector('#emails-view').append(newEmail);
			});
		});

}

function send_mail(event) {
	event.preventDefault();

	const recipients = document.querySelector('#compose-recipients').value;
	const subject = document.querySelector('#compose-subject').value;
	const body = document.querySelector('#compose-body').value;

	fetch('/emails', {
		method: 'POST',
		body: JSON.stringify({
			recipients: recipients,
			subject: subject,
			body: body
		})
	})
		.then(response => response.json())
		.then(result => {
			console.log(result);
			load_mailbox('sent')
		});

}