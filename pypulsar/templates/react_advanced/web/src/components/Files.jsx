import { useState } from 'react';
import { api } from '../utils/api';

function Files() {
  const [directory, setDirectory] = useState('.');
  const [files, setFiles] = useState([]);
  const [selectedFile, setSelectedFile] = useState('');
  const [content, setContent] = useState('');

  const handleLoadFiles = () => {
    api.call('load_files', { directory })
      .then((data) => setFiles(data.files || []))
      .catch((err) => console.error('Load files error:', err));
  };

  const handleReadFile = () => {
    if (!selectedFile) return;
    api.call('read_file', { path: selectedFile })
      .then((data) => setContent(data.content || ''))
      .catch((err) => console.error('Read file error:', err));
  };

  return (
    <div>
      <h1>Files</h1>
      <input 
        type="text" 
        value={directory} 
        onChange={(e) => setDirectory(e.target.value)} 
        placeholder="Directory path"
      />
      <button onClick={handleLoadFiles}>Load Files</button>
      <ul>
        {files.map(file => (
          <li key={file} onClick={() => setSelectedFile(file)}>{file}</li>
        ))}
      </ul>
      {selectedFile && (
        <div>
          <button onClick={handleReadFile}>Read {selectedFile}</button>
          <pre>{content}</pre>
        </div>
      )}
    </div>
  );
}

export default Files;