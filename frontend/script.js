const fileInput = document.getElementById('mdFile');
const convertBtn = document.getElementById('convertBtn');
const statusDiv = document.getElementById('status');
const fileNameDiv = document.getElementById('fileName');

// Update file name display
fileInput.addEventListener('change', function() {
	if (this.files.length > 0) {
		fileNameDiv.textContent = `Selected: ${this.files[0].name}`;
		convertBtn.disabled = false;
	} else {
		fileNameDiv.textContent = '';
		convertBtn.disabled = true;
	}
});

// Handle convert button click
convertBtn.addEventListener('click', async function() {
	if (fileInput.files.length === 0) {
		showStatus('Please select a markdown file', 'error');
		return;
	}

	const file = fileInput.files[0];
	const formData = new FormData();
	formData.append('file', file);

	try {
		showStatus('Converting markdown to HTML...', 'loading');
		convertBtn.disabled = true;

		const response = await fetch('/convert', {
			method: 'POST',
			body: formData
		});

		if (!response.ok) {
			let errorMessage = 'Conversion failed';
			const contentType = response.headers.get('content-type') || '';
			if (contentType.includes('application/json')) {
				const data = await response.json();
				errorMessage = data.error || errorMessage;
			} else {
				const text = await response.text();
				errorMessage = text || errorMessage;
			}
			throw new Error(errorMessage);
		}

		const blob = await response.blob();
		const outputFile = file.name.replace(/\.md$/i, '.html');
		const downloadUrl = window.URL.createObjectURL(blob);

		const downloadLink = document.createElement('a');
		downloadLink.href = downloadUrl;
		downloadLink.textContent = `Download ${outputFile}`;
		downloadLink.className = 'download-link';
		downloadLink.download = outputFile;
		
		showStatus(`✓ Converted ${file.name} successfully. Click the button below to download the HTML file.`, 'success');
		statusDiv.appendChild(document.createElement('br'));
		statusDiv.appendChild(downloadLink);
		setTimeout(() => window.URL.revokeObjectURL(downloadUrl), 10000);

	} catch (error) {
		showStatus(`Error: ${error.message}`, 'error');
		convertBtn.disabled = false;
	}
});

// Disable button initially if no file selected
convertBtn.disabled = true;

function showStatus(message, type) {
	statusDiv.textContent = message;
	statusDiv.className = `status ${type}`;
}
