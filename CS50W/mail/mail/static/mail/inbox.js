document.addEventListener('DOMContentLoaded', function () {

	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', compose_email);
	document.querySelector('#compose-form').addEventListener('submit', send_mail);

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
			document.querySelector('#emails-view').style.display = 'none';
			document.querySelector('#compose-view').style.display = 'none';
			document.querySelector('#email-detail-view').style.display = 'block';

			document.querySelector('#email-detail-view').innerHTML = `
				<ul style="word-break: break-all; border-radius: 15px;">
					<li class="list-group-item">
						<b style="font-size: 24px">${email.subject}</b><br>

						<div style="font-size: 16px; float: left; margin-right: 80px;"><b>From: </b>${email.sender}</div><br>
						
						<div style="font-size: 14px; float: right; margin-left: 80px;">${email.timestamp}</div>
						
						<div><b>To: </b>${email.recipients}<br></div>
					</li>
					<li class="list-group-item" style="font-size: 18px">${email.body}</li>
				</ul>
			`;

			if (!email.read) {
				fetch(`/emails/${email.id}`, {
					method: 'PUT',
					body: JSON.stringify({
						read: true
					})
				});
			}

			const archivedBtn = document.createElement('button');
			archivedBtn.innerHTML = email.archived ? "Unarchive" : "Archive";
			archivedBtn.className = email.archived ? "btn btn-success" : "btn btn-warning";
			archivedBtn.style.marginRight = '15px';
			archivedBtn.style.fontSize = '15px';

			archivedBtn.addEventListener('click', function () {
				fetch(`/emails/${email.id}`, {
					method: 'PUT',
					body: JSON.stringify({
						archived: !email.archived
					})
				})
					.then(() => { load_mailbox('archive'); });
			});
			document.querySelector('#email-detail-view').append(archivedBtn);

			const replyBtn = document.createElement('button');
			replyBtn.innerHTML = "Reply";
			replyBtn.className = "btn btn-info";
			replyBtn.style.fontSize = '15px';

			replyBtn.addEventListener('click', function () {
				compose_email();

				document.querySelector('#compose-recipients').value = email['sender'];

				let subject = email['subject'];
				if (subject.split(" ", 1)[0] != "Re:") {
					subject = "Re: " + subject;
				}
				document.querySelector('#compose-subject').value = subject;

				let body = `On ${email['timestamp']}, ${email['sender']} wrote: ${email['body']}`;
				document.querySelector('#compose-body').value = body;
			});
			document.querySelector('#email-detail-view').append(replyBtn);
			document.querySelector('#email-detail-view').style.marginBottom = '25px';
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
				newEmail.id = 'mail-box';
				newEmail.innerHTML = `
					<p id="from">${Email.sender}</p>
					<p id="time">${Email.timestamp}</p>
					<p id="sub">Subject: ${Email.subject}</p>
				`;

				newEmail.className = Email.read ? 'read' : 'unread';

				newEmail.addEventListener('click', function () {
					view_email(Email.id);
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
			load_mailbox('sent');
		});
}