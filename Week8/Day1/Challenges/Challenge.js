class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }
}

const video1 = new Video('Funny Cats Compilation', 'User123', 180);
video1.watch();

const video2 = new Video('Epic Fail Compilation', 'User456', 240);
video2.watch();

const videoData = [
    ['Nature Documentary', 'User789', 600],
    ['Cooking Tutorial', 'ChefCook', 480],
    ['Gaming Highlights', 'GamerPro', 360],
    ['Travel Vlog', 'TravelerX', 420],
    ['Educational Lecture', 'ProfessorY', 900]
];

const videos = [];
for (const [title, uploader, time] of videoData) {
    const video = new Video(title, uploader, time);
    videos.push(video);
}

videos.forEach(video => video.watch());
