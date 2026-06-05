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

		const data = await response.json();

		if (!response.ok) {
			throw new Error(data.error || 'Conversion failed');
		}

		showStatus(`✓ ${data.message}`, 'success');

		// Redirect to the converted HTML file after 1 second
		setTimeout(() => {
			window.location.href = `/export-HTML/${data.output_file}`;
		}, 1000);

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
