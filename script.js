document.addEventListener('DOMContentLoaded', () => {
    const body = document.querySelector('body');
    const header = document.querySelector('header');
    const title = document.querySelector('.title');
  
    const bgColorInput = document.getElementById('bg-color');
    const titleColorInput = document.getElementById('title-color');
    const titleSizeInput = document.getElementById('title-size');
  
    bgColorInput.addEventListener('change', () => {
      body.style.setProperty('--bg-color', bgColorInput.value);
    });
  
    titleColorInput.addEventListener('change', () => {
      header.style.setProperty('--title-color', titleColorInput.value);
    });
  
    titleSizeInput.addEventListener('change', () => {
      title.style.setProperty('--title-size', `${titleSizeInput.value}px`);
    });
  });
  