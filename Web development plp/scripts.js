/* eslint-disable linebreak-style */
document.addEventListener('DOMContentLoaded', () => {
  const optionsBtn = document.getElementById('options-btn');
  const optionsMenu = document.getElementById('options-menu');

  optionsBtn.addEventListener('click', () => {
    console.log('clicked');
    if (optionsMenu.style.display === 'none' || optionsMenu.style.display === '') {
      optionsMenu.style.display = 'block';
    } else {
      optionsMenu.style.display = 'none';
    }
  });
});
