// Study culture visual content configuration
// Only use legally cleared, self-hosted media here

// If you want to add meme images/GIFs:
// 1. Source from Pixabay (Pixabay Content License) or create original
// 2. Download and place in public/media/study-culture/
// 3. Add entry to content/media-licenses.json
// 4. Reference here as /media/study-culture/filename.ext

export type LibraryMeme = {
  id: string;
  imageUrl: string;
  title: string;
  subtitle: string;
};

export const LIBRARY_MEMES: LibraryMeme[] = [
  // Placeholder - add your own legally cleared study aesthetic images/GIFs here
  // Example:
  // {
  //   id: "study-mode",
  //   imageUrl: "/media/study-culture/study-desk.webp",
  //   title: "Study mode activated",
  //   subtitle: "Coffee + notes + determination",
  // },
];

// Text-only info cards (no external media)
export const INFO_MESSAGES = [
  {
    title: "Most repeated topics",
    subtitle: "Focus on high-yield patterns",
  },
  {
    title: "Brain not responding?",
    subtitle: "Take a break, hydrate, come back",
  },
  {
    title: "Exam in 3 days?",
    subtitle: "Hit the high-priority cards first",
  },
  {
    title: "Study tip",
    subtitle: "Teach it to understand it better",
  },
  {
    title: "96% coverage",
    subtitle: "Most repeated questions tagged",
  },
  {
    title: "Track your progress",
    subtitle: "Small wins add up",
  },
];
