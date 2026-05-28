document.addEventListener('DOMContentLoaded', () => {
    // 1. Loading Spinner on Form Submit
    const uploadForm = document.getElementById('uploadForm');
    if (uploadForm) {
        uploadForm.addEventListener('submit', () => {
            const submitBtn = document.getElementById('submitBtn');
            const btnText = submitBtn.querySelector('.btn-text');
            const spinner = document.getElementById('loadingSpinner');
            
            submitBtn.disabled = true;
            btnText.textContent = "Analyzing...";
            spinner.classList.remove('d-none');
        });
    }

    // 2. Animate Score Ring
    const scoreRing = document.querySelector('.score-ring');
    if (scoreRing) {
        const targetScore = parseInt(scoreRing.dataset.score);
        const scoreNumber = document.querySelector('.score-number');
        let currentScore = 0;
        
        const interval = setInterval(() => {
            if (currentScore >= targetScore) {
                clearInterval(interval);
            } else {
                currentScore++;
                scoreNumber.textContent = currentScore;
                scoreRing.style.background = `conic-gradient(#4f46e5 ${currentScore * 3.6}deg, #333 0deg)`;
            }
        }, 15);
    }

    // 3. Staggered Animation for Skill Badges
    const badges = document.querySelectorAll('.badge-skill');
    badges.forEach((badge, index) => {
        setTimeout(() => {
            badge.style.opacity = '1';
            badge.style.transform = 'translateY(0)';
            badge.style.transition = 'all 0.4s ease';
        }, index * 100);
    });
});
