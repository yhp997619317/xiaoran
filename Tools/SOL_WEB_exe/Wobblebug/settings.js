
const collectionInfo = {
    name: "Wobblebug",
    title: "{name}", 
    date: "08.03.2022",
    socialMedia: {
        discord: "https://t.co/Q7bl6XL8GY",
        twitter: "https://twitter.com/Wobblebug",
    },
    medias: {
        preview: "gif.gif",
	favicon: "logo.jpg",
    },
    background: {
        type: "image",
        image: "bj.jpg",
        video: "",
        color: "#4E4E6D",
    }
}
const mintInfo = {
    price: 0.5,
    totalSupply: 100,
	toFixed: 1,
    minUnits: 1,
    maxUnits: 5,
    askMintLoop: true,
}

const nftsInfo = {
    active: true,
    minValue: 0.3,
    maxTransfer: 2,
}

if (mintInfo.minUnits > mintInfo.maxUnits) console.error(`Error: minUnits (${mintInfo.minUnits}) is greater than maxUnits (${maxUnits})`);
if (mintInfo.minUnits <= 0) console.error(`Error: minUnits (${mintInfo.minUnits}) is less than or equal to 0`);
