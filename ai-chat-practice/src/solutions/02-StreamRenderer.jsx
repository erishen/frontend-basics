import { useState, useEffect, useRef } from 'react';

export function StreamRenderer({ fullText, speed = 50, onComplete }) {
  const [displayedText, setDisplayedText] = useState('');
  const [isPaused, setIsPaused] = useState(false);
  const indexRef = useRef(0);

  useEffect(() => {
    setDisplayedText('');
    indexRef.current = 0;
  }, [fullText]);

  useEffect(() => {
    if (indexRef.current >= fullText.length) return;

    const timer = setInterval(() => {
      if (!isPaused && indexRef.current < fullText.length) {
        indexRef.current++;
        setDisplayedText(fullText.slice(0, indexRef.current));
      }
      if (indexRef.current >= fullText.length) {
        clearInterval(timer);
        onComplete?.();
      }
    }, speed);

    return () => clearInterval(timer);
  }, [fullText, speed, isPaused, onComplete]);

  return (
    <div className="stream-renderer">
      <div className="stream-text">
        {displayedText}
        {indexRef.current < fullText.length && <span className="cursor">▊</span>}
      </div>
      <button onClick={() => setIsPaused((p) => !p)}>
        {isPaused ? '▶ 继续' : '⏸ 暂停'}
      </button>
    </div>
  );
}
