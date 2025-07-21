const profilePic = document.querySelector('.profile-pic');
const maxBlur = 10;

window.addEventListener('scroll', () => {
  const scrollProgress = Math.max(0, (window.scrollY - 200) / window.innerHeight);

  // Blur and scale profile pic
  profilePic.style.filter = `drop-shadow(0px 0px 10px rgba(0,0,0,0.25)) blur(${maxBlur * scrollProgress}px)`;
  profilePic.style.scale = `${Math.max(1, 1 + ((window.scrollY - 50) / 1200 * 0.5))}`;
});

// Animate projects on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, index) => {
    if (entry.isIntersecting) {
      entry.target.style.transitionDelay = `${index * 0.15}s`;
      entry.target.classList.add('appear');
    }
  });
});

document.querySelectorAll('.fadeIn').forEach(el => observer.observe(el));
