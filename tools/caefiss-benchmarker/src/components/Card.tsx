import type { MouseEvent } from "react";
import type { TranslationsType } from "../types/TranslationsType";

function Card({
  title,
  desc,
  image,
  imageName,
  imageAlt,
  requestUrl,
  trs,
  onGenerateImage,
  onDownloadImage,
}: {
  title: string;
  desc: string;
  image: string | null;
  imageName: string;
  imageAlt: string;
  requestUrl: string;
  trs: TranslationsType;
  onGenerateImage: (
    event: MouseEvent<HTMLDivElement> | MouseEvent<HTMLButtonElement>,
    requestUrl: string
  ) => void;
  onDownloadImage: (event: MouseEvent<HTMLAnchorElement>) => void;
}) {
  return (
    <>
      <div
        className="
            w-100 h-full p-5
            flex flex-col gap-5 justify-evenly
            rounded-xl 
            cursor-pointer
            bg-(--coolor-black) 
            text-md text-(--coolor-blue-light)
            shadow-[0_0_15px_rgba(0,0,0,0.4)]
            hover-glow
        "
        title={title}
        onClick={(event: MouseEvent<HTMLDivElement>) =>
          onGenerateImage(event, requestUrl)
        }
      >
        <h2 className="text-lg">{title}</h2>
        <p className="text-sm text-gray-200">{desc}</p>
        <button
          onClick={(event: MouseEvent<HTMLButtonElement>) =>
            onGenerateImage(event, requestUrl)
          }
          className="
            rounded-xl 
            shadow-[0_0_15px_rgba(0,0,0,0.4)]
            hover-glow
            py-4
            px-8
            bg-black
            cursor-pointer
            "
        >
          {trs["actions"]["generateImage"]}
        </button>
        {image && (
          <div className="flex flex-col gap-5">
            <img src={image} alt={imageAlt} className="w-100 rounded-xl" />
            <a
              onClick={(event: MouseEvent<HTMLAnchorElement>) =>
                onDownloadImage(event)
              }
              href={image}
              download={`${imageName}.png`}
              className="text-center 
                rounded-xl 
                shadow-[0_0_15px_rgba(0,0,0,0.4)]
                hover-glow
                py-4
                px-8
              bg-black
                cursor-pointer
              "
            >
              {trs["actions"]["downloadImage"]}
            </a>
          </div>
        )}
      </div>
    </>
  );
}

export default Card;
