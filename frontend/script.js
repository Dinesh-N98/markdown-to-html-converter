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

		const htmlText = await response.text();
		const outputFile = file.name.replace(/\.md$/i, '.html');
		localStorage.setItem('convertedHtml', htmlText);
		localStorage.setItem('convertedFileName', outputFile);

		const blob = new Blob([htmlText], { type: 'text/html' });
		const downloadUrl = window.URL.createObjectURL(blob);

		const previewLink = document.createElement('a');
		previewLink.href = '/preview';
		previewLink.target = '_blank';
		previewLink.rel = 'noopener noreferrer';
		previewLink.textContent = 'Preview';
		previewLink.className = 'preview-link';

		const downloadLink = document.createElement('a');
		downloadLink.href = downloadUrl;
		downloadLink.textContent = 'Download';
		downloadLink.className = 'download-link';
		downloadLink.download = outputFile;
		
		showStatus(`✓ Converted ${file.name} successfully. Click the buttons below to preview or download the HTML file.`, 'success');
		const actionRow = document.createElement('div');
		actionRow.className = 'action-links';
		actionRow.appendChild(previewLink);
		actionRow.appendChild(downloadLink);
		statusDiv.appendChild(document.createElement('br'));
		statusDiv.appendChild(actionRow);
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
