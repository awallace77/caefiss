import type { ChangeEvent } from "react";

function FileInput({
  id,
  label,
  accessibleLabel,
  onChange,
  type = "file",
  hideLabel = true,
}: {
  id: string;
  label: string;
  hideLabel: boolean;
  accessibleLabel: string;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  type: string;
}) {
  return (
    <>
      <div className="flex flex-col gap-2">
        <label
          htmlFor={id}
          className={`${hideLabel ? "hidden" : ""} text-sm text-gray-300`}
        >
          {label}
        </label>
        <input
          aria-label={accessibleLabel}
          type={type}
          id={id}
          className="w-full pl-11 px-2 py-4 
            rounded-xl  
            bg-black text-(--coolor-blue-light)
            hover-glow
            cursor-pointer
          "
          onChange={onChange}
        />
        {/* <button
          onClick={onAddFileClick}
          className="px-8 py-2 rounded-lg 
            text-md text-(--coolor-blue-light) 
            bg-(--coolor-black) 
            shadow-[0_0_15px_rgba(0,0,0,0.4)]
            hover-glow
            cursor-pointer
          "
        >
          {addFileLabel}
        </button> */}
      </div>
    </>
  );
}

export default FileInput;
